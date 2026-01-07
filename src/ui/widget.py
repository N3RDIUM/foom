from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from renderer import Renderer


class Widget:
    def __init__(self) -> None:
        pass

    def render(self, renderer: Renderer) -> None:
        _ = renderer
        pass

    def update(self) -> None:
        pass

