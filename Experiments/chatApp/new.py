import gradio as gr


def get_max_tokens() -> int:
	return 1024

def on_send(usr_msg, stats_palceholder):
	usr_msg = usr_msg or "".strip()

	try:
		resp = chat_once(usr_msg, get_max_tokens())
	except BadRequestError:
		yield "Context Limit Reached, please start a new chat or shorten inputs"

	answer = resp.choices[0].message.content or ""
	yield answer


def build_ui():
	"""Build Gradio User Interface"""
	with gr.Blocks(title="Chat with Your Model") as demo:
		gr.Markdown("## Simple Chat UI")

		chatbot = gr.Chatbot(height=350)

		with gr.Row():
			msg = gr.Textbox(placeholder="Type your message ...", scale=4)
			send_btn = gr.Button("Send", variant="primary")

		# Events
		send_event = send_btn.click(
			fn = on_send,
			inputs = [msg],
			outputs = [chatbot, msg])

	return demo


if __name__ == "__main__":
	ui = build_ui()
	host = "127.0.0.1"
	port = "7860"
	ui.queue.launch(host, port)
