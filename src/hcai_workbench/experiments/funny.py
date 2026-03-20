from . import client, console
from ..models import MODELS


def funny():
	console.print("[green]Running Funny Word Experiment[/]")

	for model in MODELS:
		console.print(f"Testing model: [blue]{model}[/]")
		response = client.chat.send(
			model=model,
			messages=[{"role": "user", "content": "What's the funniest word in the English language?."}]
		)
		console.print(f"Response from [blue]{model}[/]: {response.choices[0].message.content}\n")


if __name__ == "__main__":
	funny()
