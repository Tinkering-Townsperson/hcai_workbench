__version__ = "0.1.0"

from pathlib import Path  # noqa

from openrouter import OpenRouter
from rich.console import Console
from animation import Wait
from time import perf_counter

from .models import MODELS


def help_message(console: Console = None):
	console.print("[blue]Available commands:[/]")
	console.print("[yellow]!exit, !quit, !q, !bye[/] - Exit the application")
	console.print("[yellow]!clear, !cls[/] - Clear the console")
	console.print("[yellow]!model, !m[/] - Change the current model")
	console.print("[yellow]!config, !cfg[/] - Show configuration file location")
	console.print("[yellow]!help, !h[/] - Show this help message")


def main(model: str = "openai/gpt-5-mini", client: OpenRouter = None, console: Console = None, config_path: str = None):
	_, model_friendly_name = model.split("/")

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

		if prompt[0] == "!":
			match prompt[1:]:
				case "exit" | "quit" | "q" | "bye":
					break
				case "clear" | "cls":
					console.clear()
				case "model" | "m":
					console.print(f"Current model: [yellow]{model}[/]")
					new_model = ""

					while new_model not in MODELS:
						try:
							new_model = input("Enter new model name (e.g. openai/gpt-5-mini) or l to list: ").lower()
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
				case "help" | "h":
					help_message(console=console)
				case _:
					console.print(f"[red]Unknown command: {prompt}[/]\n")
					help_message(console=console)

			continue

		thinking = Wait((".  ", ".. ", "..."), f"{model_friendly_name} is thinking", color="blue")

		thinking.start()
		start = perf_counter()
		response = client.chat.send(
			model=model,
			messages=[
				{"role": "user", "content": prompt}
			],
			stream=False,
		)
		thinking.stop()
		end = perf_counter()

		console.print(response.choices[0].message.content)
		console.print(f"[b]=> {response.usage.total_tokens:.0f} tokens, {(end - start) * 1000:.0f} ms[/]\n")

	console.print(":wave: Goodbye!")
