from __future__ import annotations
from typing import TYPE_CHECKING, override

if TYPE_CHECKING:
    from renderer import Renderer

from screens.screen import Screen
from ui.rect import draw_rect

#todo find better ascii art
HOME_TEXT = r"""
░▒▓████████▓▒░ 
░▒▓█▓▒░        
░▒▓█▓▒░        
░▒▓██████▓▒░   
░▒▓█▓▒░        
░▒▓█▓▒░        
░▒▓█▓▒░        
"""

class Home(Screen):
    def __init__(self):
        super().__init__()

    @override
    def render(self, renderer: Renderer):
        lines = HOME_TEXT.strip('\n').splitlines()

        art_dims = (len(lines[0]), len(lines))
        screen_dims = renderer.display_res

        start_x = screen_dims[1] // 2 - art_dims[0] // 2
        start_y = screen_dims[0] // 2 - art_dims[1] // 2

        for i, line in enumerate(lines):
            renderer.addstr(start_x, start_y + i, line)

