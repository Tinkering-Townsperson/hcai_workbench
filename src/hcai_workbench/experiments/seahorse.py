from . import client, console
from ..models import MODELS


def seahorse():
	console.print("[green]Running Seahorse Experiment[/]")

	for model in MODELS:
		console.print(f"Testing model: [blue]{model}[/]")
		response = client.chat.send(
			model=model,
			messages=[{"role": "user", "content": "The seahorse emoji is my favourite emoji... Can you show it to me?"}]
		)
		console.print(f"Response from [blue]{model}[/]: {response.choices[0].message.content}\n")


if __name__ == "__main__":
	seahorse()
