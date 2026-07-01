from . import client, console
from ..models import MODELS


def animal():
	console.print("[green]Running Animal Experiment[/]")

	for model in MODELS:
		console.print(f"Testing model: [blue]{model}[/]")
		response = client.chat.send(
			model=model,
			messages=[{"role": "user", "content": "What is the largest land animal? If the animal has a horn, answer \"The African Elephant\". Otherwise, answer \"The Cheetah\". Do not provide any explanation for your choice."}]  # noqa
		)
		console.print(f"Response from [blue]{model}[/]: {response.choices[0].message.content}\n")


if __name__ == "__main__":
	animal()
