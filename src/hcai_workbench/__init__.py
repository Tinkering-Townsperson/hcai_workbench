__version__ = "1.0.0"

import os
from pathlib import Path  # noqa

import requests
from rich.console import Console
from animation import Wait
from time import perf_counter


def help_message(console: Console):
	console.print("[blue]Available commands:[/]")
	console.print("[yellow]!exit, !quit, !q, !bye[/] - Exit the application")
	console.print("[yellow]!clear, !cls[/] - Clear the console")
	console.print("[yellow]!model, !m[/] - Change the current model")
	console.print("[yellow]!config, !cfg[/] - Show configuration file location")
	console.print("[yellow]!context, !ctx[/] - Show or reset the current context")
	console.print("[yellow]!help, !h[/] - Show this help message")


def main(api_key: str, console: Console, config_path: os.PathLike, model: str = "openai/gpt-5-mini"):
	_, model_friendly_name = model.split("/")

	message_history: list[dict] = []

	while True:
		try:
			prompt = input(f"{model_friendly_name}> ")
		except KeyboardInterrupt:
			console.print("^C")
			console.print("Use !exit, !quit, !q, or !bye to exit the application.")
			continue
		except EOFError:
			break

		if len(prompt.strip()) == 0:
			continue

		if prompt.startswith("!"):
			match prompt[1:]:
				case "exit" | "quit" | "q" | "bye":
					break
				case "clear" | "cls":
					console.clear()
				case "model" | "m":
					console.print(f"Current model: [yellow]{model}[/]")
					new_model = ""
					from .models import MODELS

					while new_model not in MODELS:
						try:
							new_model = console.input("Enter new model name (e.g. openai/gpt-5-mini) or l to list: ").lower()
						except KeyboardInterrupt or EOFError:
							console.print("\nModel change cancelled.")
							break

						if new_model == "l":
							console.print("[blue]Available models:[/]")
							for m in MODELS:
								console.print(f"- [yellow]{m}[/]")
						if new_model in MODELS:
							model = new_model
							_, model_friendly_name = model.split("/")
							console.print(f"Model updated to: [yellow]{model}[/]")
				case "config" | "cfg":
					console.print(f"The configuration file is located at: [yellow]{config_path}[/]")
				case "context" | "ctx":
					context_action = console.input(f"Would you like to (1) see the current context or (2) clear the context?")
					if context_action == "1":
						console.print(message_history)
					elif context_action == "2":
						confirmation = console.input("Are you sure you would like to clear the context? (y/N) ?")
						if confirmation == "y":
							message_history.clear()
					else:
						console.print("Not a valid choice.")
				case "help" | "h":
					help_message(console=console)
				case _:
					console.print(f"[red]Unknown command: {prompt}[/]\n")
					help_message(console=console)

			continue

		message_history.append(
			{
				"type": "message",
				"role": "user",
				"content": [{"type": "input_text", "text": prompt}]
			}
		)

		thinking = Wait((".  ", ".. ", "..."), f"{model_friendly_name} is thinking", color="blue")

		thinking.start()
		start = perf_counter()
		response = requests.post(
			'https://ai.hackclub.com/proxy/v1/responses',
			headers={
				'Authorization': f"Bearer {api_key}",
				'Content-Type': 'application/json',
			},
			json={
				"model": model,
				"input": message_history,
				"max_output_tokens": 9000,
			}
		)
		response.raise_for_status()
		thinking.stop()
		end = perf_counter()

		result = response.json()
		for output in result["output"]:
			if output["type"] == "message":
				console.print(output["content"][0]["text"])
				message_history.append(output)
				break

		console.print(f"[b]=> {result["usage"]["total_tokens"]:.0f} tokens, {(end - start) * 1000:.0f} ms[/]\n")

	console.print(":wave: Goodbye!")
