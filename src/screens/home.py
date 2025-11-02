from __future__ import annotations
from typing import TYPE_CHECKING, override

if TYPE_CHECKING:
    from renderer import Renderer

from screens.screen import Screen

class Home(Screen):
    def __init__(self):
        super().__init__()

    @override
    def render(self, renderer: Renderer):
        renderer.addstr(0, 0, "Nothing.")

