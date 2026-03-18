__version__ = "0.1.0"

from pathlib import Path  # noqa

from openrouter import OpenRouter
from rich.console import Console


def main(model: str = "qwen/qwen3-32b", api_key: str = None, client: OpenRouter = None, console: Console = None):
	_, model_friendly_name = model.split("/")
	prompt = input(f"{model_friendly_name}> ")

	while prompt.lower() not in {"exit", "quit", "q", "bye"}:
		console.print(f"[blue]{model_friendly_name} is thinking...[/blue]")
		response = client.chat.send(
			model=model,
			messages=[
				{"role": "user", "content": prompt}
			],
			stream=False,
		)

		console.print(response.choices[0].message.content)
		prompt = input(f"{model_friendly_name}> ")

	console.print(":wave: Goodbye!")
