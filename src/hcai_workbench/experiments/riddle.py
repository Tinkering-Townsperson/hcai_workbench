from . import client, console
from ..models import MODELS


def riddle():
	console.print("[green]Running Riddle Experiment[/]")

	for model in MODELS:
		console.print(f"Testing model: [blue]{model}[/]")
		response = client.chat.send(
			model=model,
			messages=[{"role": "user", "content": "Albert's father has a brother called Donald. Donald has three nephews: Huey, Dewey, and... ?"}]  # noqa
		)
		console.print(f"Response from [blue]{model}[/]: {response.choices[0].message.content}\n")


if __name__ == "__main__":
	riddle()
