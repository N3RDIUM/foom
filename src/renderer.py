from curses import window, noecho, cbreak, start_color, nocbreak, endwin

class Character:
    char: str
    changed: bool

    def __init__(self, char: str = " "):
        self.char = char
        self.changed = True

class Renderer:
    display_res: tuple[int, int]
    display: list[list[Character]]
    frame: int
    in_mainloop: bool

    def __init__(self):
        self.display_res = (42, 42) # (cols, rows)
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

    def addstr(self, x: int, y: int, string: str):
        if y < 0 or y >= self.display_res[0]:
            return
        
        for i, ch in enumerate(string):
            cx = x + i
            if cx < 0 or cx >= self.display_res[1]:
                continue

            cell: Character = self.display[y][cx]
            if cell.char != ch:
                cell.char = ch
                cell.changed = True

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

