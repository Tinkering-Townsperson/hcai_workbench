from . import client, console
from ..models import MODELS


def legs():
	console.print("[green]Running Legs Experiment[/]")

	for model in MODELS:
		console.print(f"Testing model: [blue]{model}[/]")
		response = client.chat.send(
			model=model,
			messages=[{"role": "user", "content": "Five monkeys are jumping around on a four poster bed while three chickens stand and watch. How many legs are on the floor?"}]  # noqa
		)
		console.print(f"Response from [blue]{model}[/]: {response.choices[0].message.content}\n")


if __name__ == "__main__":
	legs()
