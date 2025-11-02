from curses import window, curs_set, noecho, cbreak, start_color, nocbreak, endwin

from screens.home import Home
from renderer import Renderer

class App:
    renderer: Renderer

    def __init__(self) -> None:
        self.renderer = Renderer()
        self.state = { #todo class AppState
            "screen": "home",
            "mainloop": False
        }

        self.screens = { #todo class ScreenHandler
            "home": Home()
        }

    def wrapper(self, stdscr: window) -> None:
        _ = curs_set(0)
        noecho()
        cbreak()
        start_color()

        self.state["mainloop"] = True
        while self.state["mainloop"]:
            self.screens[self.state["screen"]].render(self.renderer)
            self.renderer.drawcall(stdscr)

        nocbreak()
        endwin()

