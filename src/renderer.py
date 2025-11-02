from curses import window, color_pair
from theme import DEFAULT

class Character:
    char: str
    pair: int
    changed: bool

    def __init__(self, char: str = " ", pair: int = DEFAULT):
        self.char = char
        self.pair = pair
        self.changed = True

class Renderer:
    display_res: tuple[int, int]
    display: list[list[Character]]

    def __init__(self):
        self.display_res = (42, 42) # (cols, rows)
        self.display = []

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

    def addstr(self, x: int, y: int, string: str, pair: int = DEFAULT):
        if y < 0 or y >= self.display_res[0]:
            return
        
        for i, ch in enumerate(string):
            cx = x + i
            if cx < 0 or cx >= self.display_res[1]:
                continue

            cell: Character = self.display[y][cx]
            if cell.char != ch:
                cell.char = ch
                cell.pair = pair
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
                
                stdscr.addstr(
                    y, x, 
                    char.char,
                    color_pair(char.pair)
                )
                char.changed = False

    def drawcall(self, stdscr: window):
        res = stdscr.getmaxyx()
        if self.display_res != res:
            self.display_res = res
            self.populate_display()
        
        stdscr.nodelay(True)

        self.render(stdscr)
        stdscr.refresh()

