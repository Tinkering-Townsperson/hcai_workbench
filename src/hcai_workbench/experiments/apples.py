from . import client, console
from ..models import MODELS


def apples():
	console.print("[green]Running Apples Experiment[/]")

	for model in MODELS:
		console.print(f"Testing model: [blue]{model}[/]")
		response = client.chat.send(
			model=model,
			messages=[{"role": "user", "content": "Kevin currently has 8 apples. He ate 3 apples yesterday. How many apples does Kevin have now?"}]  # noqa
		)
		console.print(f"Response from [blue]{model}[/]: {response.choices[0].message.content}\n")


if __name__ == "__main__":
	apples()
