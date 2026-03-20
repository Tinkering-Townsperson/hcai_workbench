from . import client, console
from ..models import MODELS


def strawberry():
	console.print("[green]Running Strawberry Experiment[/]")

	for model in MODELS:
		console.print(f"Testing model: [blue]{model}[/]")
		response = client.chat.send(
			model=model,
			messages=[{"role": "user", "content": "How many Rs are in the word 'strawberry'?"}]
		)
		console.print(f"Response from [blue]{model}[/]: {response.choices[0].message.content}\n")


if __name__ == "__main__":
	strawberry()
