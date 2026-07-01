from . import client, console
from ..models import MODELS


def eggs():
	console.print("[green]Running Eggs Experiment[/]")

	for model in MODELS:
		console.print(f"Testing model: [blue]{model}[/]")
		response = client.chat.send(
			model=model,
			messages=[{"role": "user", "content": "I do not like eggs. Do I like eggs?"}]  # noqa
		)
		console.print(f"Response from [blue]{model}[/]: {response.choices[0].message.content}\n")


if __name__ == "__main__":
	eggs()
