from os import PathLike
from configparser import ConfigParser
from pathlib import Path


def validate_config(config: ConfigParser):
	assert "api_key" in config["DEFAULTS"], "API key is required in the configuration."


def set_default_config(path: PathLike) -> None:
	default_config = ConfigParser()
	default_config["DEFAULTS"] = {
		"api_key": input("Please enter your API key: "),
		"model": "openai/gpt-5-mini"
	}

	save_config(default_config, path)
	return default_config


def load_config(path: PathLike) -> dict:
	path = Path(path)

	if path.exists():
		config = ConfigParser()
		config.read(path)
	else:
		config = set_default_config(path)

	try:
		validate_config(config)
	except AssertionError as e:
		print(f"Configuration error: {e}")
		config = set_default_config(path)

	return config


def save_config(config: ConfigParser, path: PathLike) -> None:
	validate_config(config)

	path = Path(path)

	if not path.parent.exists():
		path.parent.mkdir(parents=True)

	with path.open('w') as f:
		config.write(f)
