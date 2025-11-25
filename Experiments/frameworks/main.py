from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Dict, List
from openai import OpenAI

app = FastAPI()

# CORS (ok to keep even if same-origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files under /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at root
@app.get("/")
async def index():
    return FileResponse("static/index.html")


# ---- vLLM client ----
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed",
)

user_histories: Dict[str, List[Dict[str, str]]] = {}
SYSTEM_PROMPT = "You are a helpful and concise assistant."


class ChatRequest(BaseModel):
    user_id: str
    message: str


class ChatResponse(BaseModel):
    reply: str


def build_messages(user_id: str, user_message: str) -> List[Dict[str, str]]:
    history = user_histories.get(user_id)
    if history is None:
        history = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages = history.copy()
    messages.append({"role": "user", "content": user_message})
    return messages


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    messages = build_messages(req.user_id, req.message)

    resp = client.chat.completions.create(
        model="LiquidAI/LFM2-1.2B",
        messages=messages,
        max_tokens=256,
        temperature=0.8,
        top_p=0.95,
    )

    answer = resp.choices[0].message.content

    if req.user_id not in user_histories:
        user_histories[req.user_id] = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": req.message},
            {"role": "assistant", "content": answer},
        ]
    else:
        user_histories[req.user_id].append({"role": "user", "content": req.message})
        user_histories[req.user_id].append({"role": "assistant", "content": answer})

    return ChatResponse(reply=answer)