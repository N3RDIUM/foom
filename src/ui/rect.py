from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from renderer import Renderer

def draw_rect(renderer: Renderer, x: int, y: int, w: int, h: int):
    horiz = "─"
    vert = "│"
    tl, tr, bl, br = "┌", "┐", "└", "┘"

    renderer.addstr(x + 1, y, horiz * (w - 2))
    renderer.addstr(x + 1, y + h - 1, horiz * (w - 2))

    for i in range(1, h - 1):
        renderer.addstr(x, y + i, vert)
        renderer.addstr(x + w - 1, y + i, vert)

    renderer.addstr(x, y, tl)
    renderer.addstr(x + w - 1, y, tr)
    renderer.addstr(x, y + h - 1, bl)
    renderer.addstr(x + w - 1, y + h - 1, br)

