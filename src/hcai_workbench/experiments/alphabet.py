from . import client, console
from ..models import MODELS


def alphabet():
	console.print("[green]Running Alphabet Experiment[/]")

	for model in MODELS:
		console.print(f"Testing model: [blue]{model}[/]")
		response = client.chat.send(
			model=model,
			messages=[{"role": "user", "content": "Write me a sentence where each word starts with one letter of the alphabet, going in the reverse order of the alphabet, and going through the whole alphabet."}]  # noqa
		)
		console.print(f"Response from [blue]{model}[/]: {response.choices[0].message.content}\n")


if __name__ == "__main__":
	alphabet()
