from __future__ import annotations
from typing import TYPE_CHECKING
from typing import override

from theme import DEFAULT
from ui.widget import Widget

if TYPE_CHECKING:
    from renderer import Renderer

from time import time

class Marquee(Widget):
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
        super().__init__()
        self.text = text
        self.width = width
        self.color_pair = color_pair
        self.position = position
        self.start = time()

    @override
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

        # todo make speed configurable
        speed = 6
        offset = int((diff * speed) % len(self.text))

        doubled = self.text + " " + self.text[:overflow]
        renderer.addstr(
            *self.position,
            doubled[offset:offset + self.width],
            self.color_pair
        )

