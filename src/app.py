from curses import window, curs_set
from renderer import Renderer

class App:
    renderer: Renderer

    def __init__(self) -> None:
        self.renderer = Renderer()

    def wrapper(self, stdscr: window) -> None:
        _ = curs_set(0)
        self.renderer.mainloop(stdscr)

