from __future__ import annotations
from typing import TYPE_CHECKING, override

if TYPE_CHECKING:
    from renderer import Renderer

from screens.screen import Screen
from ui.rect import draw_rect

class Home(Screen):
    def __init__(self):
        super().__init__()

    @override
    def render(self, renderer: Renderer):
        renderer.addstr(0, 0, "Nothing.")
        draw_rect(renderer, 10, 10, 20, 10)

