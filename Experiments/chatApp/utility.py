def cleanup_thinking(response):
	if not response:
		return response

	output = []
	i = 0 
	in_think = False

	while i < len(response):
		# Detect opening tag
		if response.startswith("<think>", i):
			in_think = True
			i += len({"<think>"})
			continue

		# Detect closing tag
		if response.startswith("</think>", i):
			in_think = False
			i += len("</think>")
			continue 

		if not in_think:
			output.append(response[i])

		i += 1

	cleaned = "".join(output)

	# Normalise excessive newlines
	while "\n\n\n" in cleaned:
		cleaned = cleaned.replace("\n\n\n", "\n\n")

	return cleaned.strip()


