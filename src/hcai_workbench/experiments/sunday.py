from . import client, console
from ..models import MODELS


def sunday():
	console.print("[green]Running Sunday Experiment[/]")

	for model in MODELS:
		console.print(f"Testing model: [blue]{model}[/]")
		response = client.chat.send(
			model=model,
			messages=[{"role": "user", "content": "In the year 2017, how many Sundays were there?"}]
		)
		console.print(f"Response from [blue]{model}[/]: {response.choices[0].message.content}\n")


if __name__ == "__main__":
	sunday()
