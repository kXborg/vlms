from openai import OpenAI
import gradio as gr

MAX_TURNS = 6
def build_prompt(system_msg, user_msg, assistant_msg):
	global chat_history

	if not chat_history:
        chat_history.append({
            "role": "system",
            "content": system_msg
        })
    else:
        chat_history[0] = {
            "role": "system",
            "content": system_msg
        }
        
	chat_history.append({"role":"user", "content":user_msg})
	chat_history.append({"role":"assistant","content":assistant_msg})

	system_entry = chat_history[0]
    recent = chat_history[-(MAX_TURNS * 2):]

    chat_history[:] = [system_entry] + recent

    return chat_history


def get_system_prompt(input):
	"""Define later"""
	return input

def build_query(system_prompt, input_msg, history) -> str:
	message = system_prompt + input_msg + ". Earlier context: " + history
	return message

def get_response():
	client = OpenAI(
		base_url = "https://deplorably-athonite-loreta.ngrok-free.dev/v1",
		api_key = "dummy"
		)

	response = client.chat.completions.create(
		model = "Qwen/Qwen3-0.6B",
		messages=[{"role": "user", "content": build_query()}],
		stream=True,
		)

	for chunk in response:
		delta = chunk.choices[0].delta
		if delta and delta.content:
			print(delta.content, end="", flush=True)
