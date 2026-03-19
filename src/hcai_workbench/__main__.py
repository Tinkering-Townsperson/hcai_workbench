from pathlib import Path

from openrouter import OpenRouter
from rich.console import Console

from hcai_workbench import __version__, main

from .config import load_config

# USER_DATA_DIR = Path("~/.hcai_workbench").expanduser()

CONFIG_FILE_PATH = Path.home() / "hcai_workbench.cfg"

config = load_config(CONFIG_FILE_PATH)
console = Console()

client = OpenRouter(
	api_key=config["DEFAULTS"]["api_key"],
	server_url="https://ai.hackclub.com/proxy/v1",
)


console.print(f"[green]HCAI Workbench [b]v{__version__}[/]")
main(model=config["DEFAULTS"]["model"], client=client, console=console, config_path=CONFIG_FILE_PATH)
