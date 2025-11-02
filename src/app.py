from curses import window, curs_set, noecho, cbreak, start_color, nocbreak, endwin

from screens.screen import Screen
from screens.home import Home
from renderer import Renderer

class AppState:
    screen: str
    mainloop: bool

    def __init__(self) -> None:
        self.screen = "home"
        self.mainloop = False

class StatusBar:
    def __init__(self) -> None:
        pass

    def render(self, renderer: Renderer):
        last_line = renderer.display_res[0] - 1
        renderer.addstr(0, last_line, "A")

class App:
    renderer: Renderer
    state: AppState
    statusbar: StatusBar

    def __init__(self) -> None:
        self.renderer = Renderer()
        self.state = AppState()
        self.statusbar = StatusBar()

        self.screens: dict[str, Screen] = {
            "home": Home()
        }

    def wrapper(self, stdscr: window) -> None:
        _ = curs_set(0)
        noecho()
        cbreak()
        start_color()

        self.state.mainloop = True
        while self.state.mainloop:
            self.screens[self.state.screen].render(self.renderer)
            self.statusbar.render(self.renderer)

            self.renderer.drawcall(stdscr)

        nocbreak()
        endwin()

