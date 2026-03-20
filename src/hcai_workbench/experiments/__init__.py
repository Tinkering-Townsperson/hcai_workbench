from pathlib import Path

from openrouter import OpenRouter
from rich.console import Console

from ..config import load_config

CONFIG_FILE_PATH = Path.home() / "hcai_workbench.cfg"

config = load_config(CONFIG_FILE_PATH)
console = Console()

client = OpenRouter(
	api_key=config["DEFAULTS"]["api_key"],
	server_url="https://ai.hackclub.com/proxy/v1",
)
