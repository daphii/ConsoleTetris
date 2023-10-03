color_codes = {
    "I": '\033[96m',
    "J": '\033[94m',
    "L": '\033[36m',
    "O": '\033[93m',
    "S": '\033[92m',
    "Z": '\033[91m',
    "T": '\033[95m'
}

class GameSpace:
    def __init__(self, x, y) -> None:
        self.empty = True
        self.location = (x, y)
        self.piece_code = ""

    def display(self) -> str:
        display = ""
        if self.empty:
            display = " . "
        else:
            color_code = color_codes[self.piece_code]
            display = color_code + f"[{self.piece_code}]" + '\033[0m'
        return display
    
    def set_piece(self, code):
        self.empty = False
        self.piece_code = code

    def clear_piece(self):
        self.empty = True
        self.piece_code = ""

class GameBoard:
    def __init__(self) -> None:
        self.height = 20
        self.width = 10
        self.make_board()

    def make_board(self):
        self.rows = []
        for i in range(self.height):
            row = [GameSpace(j, i) for j in range(self.width)]
            self.rows.append(row)

    def display_board(self):
        display = ""
        for i in range(len(self.rows)):
            row_display = ""
            for j in range(len(self.rows[i])):
                row_display += self.rows[i][j].display()
            display += row_display + "\n"
        print(display)