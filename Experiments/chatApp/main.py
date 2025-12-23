import mimetypes
import gradio as gr
from PIL import Image
from pathlib import Path
import os, re, base64, requests, io
from typing import Dict, List
from openai import OpenAI, BadRequestError, NotFoundError

# Environment / Defaults
BASE_DIR = Path(__file__).parent
openai_api_key = os.getenv("OPENAI_API_KEY", "EMPTY")
# Modify the base URL depending on host
# openai_api_base = os.getenv("OPENAI_API_BASE", "http://localhost:8000/v1")
openai_api_base = os.getenv("OPENAI_API_BASE", "http://192.168.0.30:8000/v1")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "")
VISION_MODELS_ENV = {m.strip() for m in os.getenv("VISION_MODELS", "").split(",") if m.strip()}

DEFAULT_MAX_TOKENS = int(os.getenv("MAX_TOKENS", "4096"))
MAX_TOKENS_VISION = int(os.getenv("MAX_TOKENS_VISION", "1024"))
MAX_HISTORY_TURNS = int(os.getenv("MAX_HISTORY_TURNS", "6"))
MAX_HISTORY_TURNS_TEXT = int(os.getenv("MAX_HISTORY_TURNS_TEXT", "6"))
MAX_HISTORY_TURNS_VISION = int(os.getenv("MAX_HISTORY_TURNS_VISION", "2"))
CONTEXT_MARGIN = int(os.getenv("CONTEXT_MARGIN", "16"))
SUFFIX_MARGIN_TOKENS = int(os.getenv("SUFFIX_MARGIN_TOKENS", "24"))
TRUNCATION_SUFFIX = os.getenv("TRUNCATION_SUFFIX", "… Would you like me to continue?")

client = OpenAI(api_key=openai_api_key, base_url=openai_api_base)

# Image compression / sizing settings (match app/main.py behavior)
IMAGE_SIZE_THRESHOLD = int(os.getenv("IMAGE_SIZE_THRESHOLD", str(500 * 1024)))
IMAGE_MAX_SIZE_THRESHOLD = int(os.getenv("IMAGE_MAX_SIZE_THRESHOLD", str(1 * 1024 * 1024)))
IMAGE_MAX_DIMENSION = int(os.getenv("IMAGE_MAX_DIMENSION", "2048"))
IMAGE_QUALITY = int(os.getenv("IMAGE_QUALITY", "85"))

# Vision capability cache (match app/main.py behavior)
VISION_PROBE_CACHE = {}

# Helper functions
def probe_vision_capability(base_url, model_id, timeout = 5):
    """Probe model for vision capability by attempting a test request with an image."""
    if model_id in VISION_PROBE_CACHE:
        return VISION_PROBE_CACHE[model_id]

    payload = {
        "model": model_id,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": "about:blank"},
                    {"type": "text", "text": "ping"},
                ],
            }
        ],
        "max_tokens": 1,
    }

    try:
        r = requests.post(
            f"{base_url}/chat/completions",
            json=payload,
            timeout=timeout,
        )

        if r.status_code == 200:
            VISION_PROBE_CACHE[model_id] = True
            return True

        error_text = r.text.lower()

        if any(k in error_text for k in [
            "image",
            "vision",
            "multimodal",
            "image_url",
            "image token",
        ]):
            VISION_PROBE_CACHE[model_id] = True
            return True

        VISION_PROBE_CACHE[model_id] = False
        return False

    except requests.RequestException:
        VISION_PROBE_CACHE[model_id] = False
        return False


def get_max_tokens_for_model(model_id):
    """Get appropriate max output tokens based on model type."""
    return MAX_TOKENS_VISION if probe_vision_capability(openai_api_base, model_id) else DEFAULT_MAX_TOKENS


def get_max_history_turns_for_model(model_id):
    """Get appropriate max history turns based on model type."""
    return MAX_HISTORY_TURNS_VISION if probe_vision_capability(openai_api_base, model_id) else MAX_HISTORY_TURNS_TEXT


def _parse_allowed_tokens_from_error(msg):
    try:
        max_ctx_match = re.search(r"maximum context length is (\d+) tokens", msg)
        input_match = re.search(r"your request has (\d+) input tokens", msg)
        if not max_ctx_match or not input_match:
            return None
        max_ctx = int(max_ctx_match.group(1))
        input_tokens = int(input_match.group(1))
        allowed = max_ctx - input_tokens - CONTEXT_MARGIN
        return allowed if allowed > 0 else 0
    except Exception:
        return None


def _read_text_file(path, limit = 20000):
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:limit]
    except Exception:
        return None


def _to_data_url(path, mime):
    try:
        # If image is large, attempt to compress/resize in-place before encoding
        if mime.startswith("image/"):
            try:
                compress_image(path, mime)
            except Exception:
                # ignore compression errors and fall back to raw bytes
                pass
    except Exception:
        pass
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{b64}"


def compress_image(file_path, mime_type):
    """
    Compress image in-place if it exceeds size threshold.
    Resizes large images and re-encodes with quality tuning.
    """
    try:
        file_size = file_path.stat().st_size
        if file_size < IMAGE_SIZE_THRESHOLD:
            return  # No compression needed

        img = Image.open(file_path)

        # Convert RGBA/LA/P to RGB if saving as JPEG (JPEG doesn't support transparency)
        if img.mode in ("RGBA", "LA", "P"):
            if mime_type in ("image/jpeg", "application/octet-stream"):
                rgb_img = Image.new("RGB", img.size, (255, 255, 255))
                if img.mode == "RGBA":
                    rgb_img.paste(img, mask=img.split()[-1])
                else:
                    rgb_img.paste(img)
                img = rgb_img

        # Resize if dimensions are too large
        if img.width > IMAGE_MAX_DIMENSION or img.height > IMAGE_MAX_DIMENSION:
            img.thumbnail((IMAGE_MAX_DIMENSION, IMAGE_MAX_DIMENSION), Image.Resampling.LANCZOS)

        # Determine output format and quality
        if mime_type == "image/png":
            output_format = "PNG"
            save_kwargs = {"optimize": True}
        elif mime_type == "image/webp":
            output_format = "WEBP"
            save_kwargs = {"quality": IMAGE_QUALITY}
        else:  # Default to JPEG for unknown/JPEG types
            output_format = "JPEG"
            save_kwargs = {"quality": IMAGE_QUALITY, "optimize": True}

        # Save to in-memory buffer first to check size
        buffer = io.BytesIO()
        img.save(buffer, format=output_format, **save_kwargs)
        compressed_size = buffer.tell()

        # Only write back if compressed size is smaller
        if compressed_size < file_size:
            buffer.seek(0)
            file_path.write_bytes(buffer.getvalue())

    except Exception as e:
        # Log error but don't fail flow if compression fails
        print(f"Warning: Image compression failed for {file_path.name}: {e}")


def _build_attachments(files):
    """Convert uploaded files to attachment dicts: {filename, url, mime_type, text?}
    - Text files: add text preview
    - Images: use data: URL so some servers can read them (may not work everywhere)
    - PDFs: referenced by filename only
    """
    results= []
    for f in files or []:
        if f is None:
            continue
        # Normalize Gradio Files data: could be dict, object with attributes, or str path
        fname = None
        mime = None
        if isinstance(f, dict):
            fname = f.get("name") or f.get("path") or f.get("orig_name")
            mime = f.get("mime_type")
        elif isinstance(f, (str, os.PathLike)):
            fname = str(f)
        else:
            # object with attributes
            fname = getattr(f, "name", None) or getattr(f, "path", None)
            mime = getattr(f, "mime_type", None)

        if not fname:
            continue
        p = Path(str(fname))
        name = p.name
        ext = p.suffix.lower()
        if not mime:
            guessed, _ = mimetypes.guess_type(str(p))
            mime = guessed or "application/octet-stream"
        item = {"filename": name, "mime_type": mime}
        if ext in {".txt", ".md", ".markdown"}:
            txt = _read_text_file(p)
            item["text"] = txt[:5000] if txt else None
            item["url"] = name
        elif mime.startswith("image/"):
            try:
                item["url"] = _to_data_url(p, mime)
            except Exception:
                item["url"] = name
        else:
            item["url"] = name
        results.append(item)
    return results


def _merge_text_for_text_only(base_text, attachments):
    if not attachments:
        return base_text
    lines= []
    for att in attachments:
        header = f"[Attachment] {att.get('filename','')} ({att.get('mime_type','')}) URL: {att.get('url','')}"
        if att.get("text"):
            preview = att["text"][:5000]
            header += f"\nContent preview:\n{preview}"
        lines.append(header)
    return base_text + "\n\n" + "\n\n".join(lines)


def _build_user_content(user_message, attachments, model_id):
    if probe_vision_capability(openai_api_base, model_id):
        parts = [{"type": "text", "text": user_message}]
        for att in attachments or []:
            mt = (att.get("mime_type") or "").lower()
            if mt.startswith("image/") and att.get("url"):
                parts.append({"type": "image_url", "image_url": {"url": att["url"]}})
            elif mt.startswith("text/") and att.get("text"):
                parts.append({"type": "text", "text": f"[Attachment {att.get('filename','')}]\n{att['text'][:5000]}"})
        return parts
    return _merge_text_for_text_only(user_message, attachments)


def _trim_history(history_msgs, model_id = ""):
    """Trim history to keep system + last N turns (user+assistant) based on model type."""
    if not history_msgs:
        return []
    system = history_msgs[:1] if history_msgs[0].get("role") == "system" else []
    tail = history_msgs[1:] if system else history_msgs
    max_turns = get_max_history_turns_for_model(model_id)
    max_tail = max_turns * 2
    return [*system, *tail[-max_tail:]]


def list_models():
    items = []
    default_id = DEFAULT_MODEL if DEFAULT_MODEL else None
    try:
        data = client.models.list()
        for m in getattr(data, "data", []) or []:
            mid = getattr(m, "id", None) or getattr(m, "model", None) or ""
            if isinstance(mid, str) and mid:
                items.append(mid)
        if items and not default_id:
            default_id = items[0]
    except Exception:
        pass
    return items, default_id

# Core chat logic (used by Gradio events)

def chat_once(messages, model_name, max_tokens):
    effective_max_tokens = max(16, max_tokens - SUFFIX_MARGIN_TOKENS)
    try:
        return client.chat.completions.create(
            model=model_name,
            messages=messages,
            max_tokens=effective_max_tokens,
            temperature=0.8,
            top_p=0.95,
        )
    except BadRequestError as e:
        allowed = _parse_allowed_tokens_from_error(str(e))
        if allowed is None:
            effective_max_tokens = max(16, effective_max_tokens // 2)
        else:
            effective_max_tokens = max(16, min(effective_max_tokens, allowed - max(0, SUFFIX_MARGIN_TOKENS)))
        return client.chat.completions.create(
            model=model_name,
            messages=messages,
            max_tokens=effective_max_tokens,
            temperature=0.8,
            top_p=0.95,
        )


def chat_stream(messages, model_name, max_tokens):
    effective_max_tokens = max(16, max_tokens - SUFFIX_MARGIN_TOKENS)

    def do_stream(toks):
        return client.chat.completions.create(
            model=model_name,
            messages=messages,
            max_tokens=toks,
            temperature=0.8,
            top_p=0.95,
            stream=True,
        )

    try:
        return do_stream(effective_max_tokens)
    except BadRequestError as e:
        allowed = _parse_allowed_tokens_from_error(str(e))
        if allowed is None:
            effective_max_tokens = max(16, effective_max_tokens // 2)
        else:
            effective_max_tokens = max(16, min(effective_max_tokens, allowed - max(0, SUFFIX_MARGIN_TOKENS)))
        try:
            return do_stream(effective_max_tokens)
        except BadRequestError:
            raise

# Gradio UI / Handlers

def on_load_models():
    models, default_id = list_models()
    label = "Model" if models else "Model (Not Available)"
    return gr.update(choices=models, value=default_id, visible=True, label=label), (default_id or "")


def on_reset():
    return [], "", ""


def on_send(user_msg,
    files: List[gr.File],
    history: List[Dict[str, str]],
    selected_model: str,
    system_prompt: str,
    stream: bool,
    stats_placeholder: str,
):
    user_msg = (user_msg or "").strip()
    if not selected_model:
        yield history, "", " Model Not Available. Click Refresh Models and try again."
        return
    if not user_msg and not files:
        yield history, "", stats_placeholder
        return

    # Build attachments and model-aware user content
    atts = _build_attachments(files)
    history_msgs = []
    if system_prompt:
        history_msgs.append({"role": "system", "content": system_prompt})
    # Convert history into OpenAI message format
    for msg in history:
        if isinstance(msg, dict):
            # Already in dict format from Gradio's new Chatbot
            if msg.get("role") and msg.get("content"):
                history_msgs.append(msg)
        else:
            # Legacy tuple format (user, assistant)
            u, a = msg
            history_msgs.append({"role": "user", "content": u})
            if a:
                history_msgs.append({"role": "assistant", "content": a})
    history_msgs = _trim_history(history_msgs, selected_model)
    history_msgs.append({"role": "user", "content": _build_user_content(user_msg, atts, selected_model)})

    if not stream:
        try:
            resp = chat_once(history_msgs, selected_model, get_max_tokens_for_model(selected_model))
        except NotFoundError:
            yield history, "", f" Model '{selected_model}' not found on server."
            return
        except BadRequestError:
            yield history, "", " Context limit reached. Please start a new chat or shorten input."
            return
        answer = resp.choices[0].message.content or ""
        finish_reason = getattr(resp.choices[0], "finish_reason", None)
        if finish_reason == "length" and TRUNCATION_SUFFIX:
            answer = f"{answer}{TRUNCATION_SUFFIX}"
        usage = getattr(resp, "usage", None)
        prompt_tokens = getattr(usage, "prompt_tokens", None)
        completion_tokens = getattr(usage, "completion_tokens", None)
        total_tokens = getattr(usage, "total_tokens", None)
        history = history + [{"role": "user", "content": user_msg}, {"role": "assistant", "content": answer}]
        stats = []
        if prompt_tokens is not None: stats.append(f"prompt={prompt_tokens}")
        if completion_tokens is not None: stats.append(f"completion={completion_tokens}")
        if total_tokens is not None: stats.append(f"total={total_tokens}")
        stats_text = " • ".join(stats)
        yield history, "", (f"Tokens: {stats_text}" if stats_text else "")
        return

    # Streaming path
    history = history + [{"role": "user", "content": user_msg}, {"role": "assistant", "content": ""}]  # append empty assistant and update progressively
    try:
        stream_resp = chat_stream(history_msgs, selected_model, get_max_tokens_for_model(selected_model))
    except NotFoundError:
        history = history[:-2]  # Remove the user and assistant messages we just added
        yield history, "", f" Model Not Available on server."
        return
    except BadRequestError:
        history = history[:-2]  # Remove the user and assistant messages we just added
        yield history, "", " Context limit reached. Please start a new chat or shorten input."
        return

    buffer = []
    last_finish = None
    import time
    start_t = time.perf_counter()

    for chunk in stream_resp:
        choice0 = chunk.choices[0]
        last_finish = getattr(choice0, "finish_reason", last_finish)
        delta = getattr(choice0, "delta", None)
        piece = getattr(delta, "content", None) or ""
        if piece:
            buffer.append(piece)
            # Update the last assistant message progressively
            history[-1]["content"] = "".join(buffer)
            yield history, "", stats_placeholder

    final_answer = "".join(buffer)
    if last_finish == "length" and TRUNCATION_SUFFIX:
        final_answer = f"{final_answer}{TRUNCATION_SUFFIX}"
        history[-1]["content"] = final_answer
        yield history, "", stats_placeholder

    end_t = time.perf_counter()
    dur = end_t - start_t
    approx_tokens = max(1, len(final_answer) // 4)
    tps = approx_tokens / max(0.001, dur)
    stats = f"duration_ms={int(dur*1000)} • approx_tokens={approx_tokens} • tokens_per_sec={tps:.2f}"
    yield history, "", stats


def build_ui():
    with gr.Blocks(title="Chat with Your Model") as demo:
        gr.Markdown("## Chat with Your Model")

        with gr.Row():
            model_dd = gr.Dropdown(choices=[], value=None, label="Model", scale=3)
            refresh_btn = gr.Button("Refresh Models", scale=1)
            reset_btn = gr.Button("Reset", scale=1)

        system_prompt = gr.Textbox(value="You are a helpful assistant.", label="System Prompt", lines=2)
        chatbot = gr.Chatbot(height=350)
        stats = gr.Markdown(visible=True)

        with gr.Row():
            msg = gr.Textbox(placeholder="Type your message...", scale=4)
            files = gr.Files(label="Attach files (txt, md, images, pdf)", file_count="multiple")
            stream_ck = gr.Checkbox(value=True, label="Stream")
            send_btn = gr.Button("Send", variant="primary")

        # Session states
        history_state = gr.State([])  # List[Tuple[user, assistant]]
        model_state = gr.State("")

        # Events
        demo.load(on_load_models, outputs=[model_dd, model_state])
        refresh_btn.click(on_load_models, outputs=[model_dd, model_state])

        reset_btn.click(on_reset, inputs=None, outputs=[chatbot, msg, stats])
        reset_btn.click(lambda: [], None, history_state)

        # Send handler with stream generator
        send_event = send_btn.click(
            fn=on_send,
            inputs=[msg, files, history_state, model_dd, system_prompt, stream_ck, stats],
            outputs=[chatbot, msg, stats],
        )
        # Keep history_state synchronized after each yield
        send_event.then(lambda h, m, s: h, [chatbot, msg, stats], history_state)

    return demo


if __name__ == "__main__":
    ui = build_ui()
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "7860"))
    ui.queue().launch(server_name=host, server_port=port)
