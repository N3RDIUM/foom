from curses import *
from time import sleep

class Character:
    char: str
    changed: bool

    def __init__(self, char = " "):
        self.char = char
        self.changed = True

class Renderer:
    def __init__(self):
        self.display_res = (42, 42)
        self.display = []

        self.frame = 0
        self.in_mainloop = False

        self.populate_display()

    def populate_display(self):
        new_display = []

        for _ in range(self.display_res[0]):
            row = []

            for _ in range(self.display_res[1]):
                char = " "
                row.append(Character(char))

            new_display.append(row)

        del self.display
        self.display = new_display

    def render(self, stdscr: window):
        for y in range(self.display_res[0]):
            for x in range(self.display_res[1]):
                char = self.display[y][x]
                if not char.changed:
                    continue

                if y == self.display_res[0] - 1:
                    if x == self.display_res[1] - 1:
                        continue
                
                stdscr.addstr(y, x, char.char)
                char.changed = False

    def debug(self, stdscr: window):
        debug_string = f"debug {self.frame}"
        stdscr.addstr(
            self.display_res[0] - 1, 
            self.display_res[1] - len(debug_string) - 1,
            debug_string
        )

    def drawcall(self, stdscr: window):
        res = stdscr.getmaxyx()
        if self.display_res != res:
            self.display_res = res
            self.populate_display()
        
        stdscr.nodelay(True)

        self.render(stdscr)
        self.debug(stdscr)
        
        self.frame += 1
        stdscr.refresh()

    def mainloop(self, stdscr: window):
        noecho()
        cbreak()
        start_color()

        self.in_mainloop = True
        while self.in_mainloop:
            self.drawcall(stdscr)

        nocbreak()
        endwin()

