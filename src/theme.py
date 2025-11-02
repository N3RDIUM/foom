import json
from curses import init_color, init_pair
from config import config

# color enum
FOREGROUND = 1
BACKGROUND = 2

# pair enum
DEFAULT = 1

def process_color(color: str) -> tuple[int, int, int]:
    ret = int(color.strip("#"), 16)
    ret = (ret >> 16) & 0xFF, (ret >> 8) & 0xFF, ret & 0xFF
    return (
        int(ret[0] / 256 * 1000),
        int(ret[1] / 256 * 1000),
        int(ret[2] / 256 * 1000),
    )

def load_theme() -> None:
    theme_path: str = config["theme"]
    theme = json.load(open(f"themes/{theme_path}.json"))

    init_color(BACKGROUND, *process_color(theme["background"]))
    init_color(FOREGROUND, *process_color(theme["foreground"]))

    init_pair(DEFAULT, FOREGROUND, BACKGROUND)

