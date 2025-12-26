from openai import OpenAI
import gradio as gr
from utility import cleanup_thinking

MAX_TURNS = 6
chat_history = []

client = OpenAI(
	base_url ="https://fatima-nonhyperbolical-parallel.ngrok-free.dev/v1",
	api_key="dummy"
	)

def build_prompt(system_msg, user_msg):
	global chat_history
	if not chat_history:
		chat_history.append({"role": "system", "content": system_msg })
	
	chat_history.append({"role":"user", "content":user_msg})

	# Keep only last N Turns
	system_entry = chat_history[0]
	turns = chat_history[1:]

	trimmed = turns[-(MAX_TURNS * 2):]

	chat_history[:] = [system_entry] + trimmed

	print(chat_history)

	return chat_history


def chat_handler(message, history):
	global chat_history
	system_prompt = "You are a helpful assistant."
	messages = build_prompt(system_prompt, message)

	stream = client.chat.completions.create(
		model="Qwen/Qwen3-0.6B",
		messages=messages,
		stream=True,)

	partial = ""

	for chunk in stream:
		delta = chunk.choices[0].delta
		if delta and delta.content:
			partial += delta.content
			yield partial

	cleaned = cleanup_thinking(partial)

	chat_history.append({"role":"assistant", "content": cleaned})



def build_ui():

	demo_app = gr.ChatInterface(
		fn = chat_handler,
		title = "Simple Chat UI",
		description = "Streaming Chat using OpenAI-compatible API",
	)

	demo_app.launch()


if __name__ == "__main__":
	build_ui()

