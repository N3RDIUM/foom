from __future__ import annotations
from typing import TYPE_CHECKING

from theme import DEFAULT

if TYPE_CHECKING:
    from renderer import Renderer

from time import time

#todo widget baseclass
class ScrollText:
    text: str
    width: int
    color_pair: int
    position: tuple[int, int]
    start: float

    def __init__(
        self, 
        text: str,
        width: int = 42,
        color_pair: int = DEFAULT,
        position: tuple[int, int] = (0, 0)
    ) -> None:
        self.text = text
        self.width = width
        self.color_pair = color_pair
        self.position = position
        self.start = time()

    def render(self, renderer: Renderer) -> None:
        overflow = len(self.text) - self.width
        if overflow <= 0:
            renderer.addstr(
                *self.position,
                self.text,
                self.color_pair
            )
            return

        current = time()
        diff = current - self.start
        offset = int((diff * 6) % len(self.text))

        doubled = self.text + " " + self.text
        renderer.addstr(
            *self.position,
            doubled[offset:offset + self.width],
            self.color_pair
        )
