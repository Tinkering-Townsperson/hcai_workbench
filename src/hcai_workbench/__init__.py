__version__ = "0.1.0"

from pathlib import Path

from openrouter import OpenRouter

from .config import load_config
from .models import MODELS  # noqa


USER_DATA_DIR = Path("~/.hcai_workbench").expanduser()
CONFIG_FILE_PATH = USER_DATA_DIR / "settings.toml"

config = load_config(CONFIG_FILE_PATH)

client = OpenRouter(
	api_key=config["api_key"],
	server_url="https://ai.hackclub.com/proxy/v1",
)


def main(model: str = "qwen/qwen3-32b"):
	_, model_friendly_name = model.split("/")
	prompt = input(f"{model_friendly_name}> ")

	while prompt.lower() != "q":
		print(f"{model_friendly_name} is thinking...")
		response = client.chat.send(
			model=model,
			messages=[
				{"role": "user", "content": prompt}
			],
			stream=False,
		)

		print(response.choices[0].message.content)
		prompt = input(f"{model_friendly_name}> ")

	print("Goodbye!")
