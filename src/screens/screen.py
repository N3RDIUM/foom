from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from renderer import Renderer

class Screen:
    def __init__(self):
        print("hi")

    def render(self, renderer: Renderer):
        pass

