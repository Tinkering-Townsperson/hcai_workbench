from configparser import ConfigParser
from importlib import import_module
from pathlib import Path
import tempfile

import pytest

from hcai_workbench.config import load_config, save_config, validate_config


class _FakeResponse:
	def raise_for_status(self):
		return None

	def json(self):
		return {
			"data": [
				{"id": "openai/gpt-5-mini", "architecture": {"output_modalities": ["text"]}},
				{"id": "openai/gpt-5-vision", "architecture": {"output_modalities": ["text", "image"]}},
				{"id": "anthropic/claude-sonnet", "architecture": {"output_modalities": ["text"]}},
			]
		}


def test_version_and_model_loading(monkeypatch):
	import requests

	monkeypatch.setattr(requests, "get", lambda *args, **kwargs: _FakeResponse())
	hcai_workbench = import_module("hcai_workbench")
	models_module = import_module("hcai_workbench.models")

	assert hcai_workbench.__version__ == "1.0.0"
	assert models_module.MODELS == ["anthropic/claude-sonnet", "openai/gpt-5-mini"]


def test_validate_config_requires_api_key():
	config = ConfigParser()
	config["DEFAULTS"] = {"model": "openai/gpt-5-mini"}

	with pytest.raises(AssertionError, match="API key is required"):
		validate_config(config)


def test_load_config_creates_and_saves_defaults(monkeypatch):
	with tempfile.TemporaryDirectory(dir=Path.cwd()) as temp_dir:
		config_path = Path(temp_dir) / "hcai_workbench.cfg"
		monkeypatch.setattr("builtins.input", lambda prompt="": "test-api-key")
		config = load_config(config_path)

		assert config["DEFAULTS"]["api_key"] == "test-api-key"
		assert config["DEFAULTS"]["model"] == "openai/gpt-5-mini"
		assert config_path.exists()


def test_save_config_writes_expected_file():
	with tempfile.TemporaryDirectory(dir=Path.cwd()) as temp_dir:
		config_path = Path(temp_dir) / "hcai_workbench.cfg"
		config = ConfigParser()
		config["DEFAULTS"] = {"api_key": "abc123", "model": "openai/gpt-5-mini"}

		save_config(config, config_path)

		assert config_path.read_text().strip() == "[DEFAULTS]\napi_key = abc123\nmodel = openai/gpt-5-mini"
