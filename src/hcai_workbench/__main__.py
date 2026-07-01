from pathlib import Path

from rich.console import Console

from hcai_workbench import __version__, main
from hcai_workbench.config import load_config

# USER_DATA_DIR = Path("~/.hcai_workbench").expanduser()

CONFIG_FILE_PATH = Path.home() / "hcai_workbench.cfg"

config = load_config(CONFIG_FILE_PATH)
console = Console()


console.print(f"[green]HCAI Workbench [b]v{__version__}[/]")
main(api_key=config["DEFAULTS"]["api_key"], console=console, config_path=CONFIG_FILE_PATH, model=config["DEFAULTS"]["model"])
