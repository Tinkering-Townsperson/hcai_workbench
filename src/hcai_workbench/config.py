from tomlkit import load, dump
from pathlib import Path


def validate_config(config: dict):
	assert "api_key" in config["defaults"], "API key is required in the configuration."


def set_default_config(path: str) -> None:
	default_config = {
		"defaults": {
			"api_key": input("Please enter your API key: "),
			"model": "openai/gpt-5-mini"
		}
	}

	save_config(default_config, path)
	return default_config


def load_config(path: str) -> dict:
	path = Path(path)

	if path.exists():
		with path.open('r') as f:
			config = load(f)
	else:
		config = set_default_config(path)

	try:
		validate_config(config)
	except AssertionError as e:
		print(f"Configuration error: {e}")
		config = set_default_config(path)

	return config


def save_config(config: dict, path: str) -> None:
	validate_config(config)

	path = Path(path)

	if not path.parent.exists():
		path.parent.mkdir(parents=True)

	with path.open('w') as f:
		dump(config, f)
