from pathlib import Path

from openrouter import OpenRouter
from rich.console import Console

from hcai_workbench import __version__, main

from .config import load_config
from .models import MODELS  # noqa

USER_DATA_DIR = Path("~/.hcai_workbench").expanduser()
CONFIG_FILE_PATH = USER_DATA_DIR / "settings.toml"

config = load_config(CONFIG_FILE_PATH)
console = Console()

client = OpenRouter(
	api_key=config["defaults"]["api_key"],
	server_url="https://ai.hackclub.com/proxy/v1",
)


console.print(f"[green]HCAI Workbench [b]v{__version__}[/]")
main(model=config["defaults"]["model"], client=client, console=console)
