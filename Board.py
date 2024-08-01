from Const import *

class Board:

    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range COLS]

        self._create_()
    def _create_(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def __add__pieces(self, color):
        pass