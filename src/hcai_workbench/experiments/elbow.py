from . import client, console
from ..models import MODELS


def elbow():
	console.print("[green]Running Elbow Experiment[/]")

	for model in MODELS:
		console.print(f"Testing model: [blue]{model}[/]")
		response = client.chat.send(
			model=model,
			messages=[{"role": "user", "content": "What is elbow spelled backwards?"}]  # noqa
		)
		console.print(f"Response from [blue]{model}[/]: {response.choices[0].message.content}\n")


if __name__ == "__main__":
	elbow()
