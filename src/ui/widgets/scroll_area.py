from __future__ import annotations
from typing import TYPE_CHECKING

from ui.widget import Widget

if TYPE_CHECKING:
    from renderer import Renderer

class ScrollArea:
    widget: Widget

    def __init__(self, widget: Widget) -> None:
        self.widget = widget

