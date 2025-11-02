from curses import window, curs_set, noecho, cbreak, start_color, nocbreak, endwin
from time import time, sleep

from theme import load_theme
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
    state: AppState

    def __init__(self, state: AppState) -> None:
        self.state = state

    def render(self, renderer: Renderer):
        # todo player state, keybinds, etc.

        last_line = renderer.display_res[0] - 1
        last_line_text = f"{self.state.screen}"
        renderer.addstr(0, last_line, last_line_text)

class App:
    renderer: Renderer
    state: AppState
    statusbar: StatusBar

    def __init__(self) -> None:
        self.renderer = Renderer()
        self.state = AppState()
        self.statusbar = StatusBar(self.state)

        self.screens: dict[str, Screen] = {
            "home": Home()
        }

    def wrapper(self, stdscr: window) -> None:
        _ = curs_set(0)
        noecho()
        cbreak()

        start_color()
        load_theme()

        self.state.mainloop = True
        while self.state.mainloop:
            t0 = time()

            self.screens[self.state.screen].render(self.renderer)
            self.statusbar.render(self.renderer)

            self.renderer.drawcall(stdscr)

            spent = time() - t0
            minimum = 1 / 60

            # fps cap
            if spent < minimum:
                sleep(minimum - spent)

        nocbreak()
        endwin()

