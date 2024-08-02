import os
from Piece import *
from Const import *

class Board:

    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range COLS]

        self._create_()
        self.__add__pieces('white')
        self.__add__pieces('black')
    def _create_(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def __add__pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # Pawns -- 8
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # Knights -- 2
            self.squares(row_other)[1] = Square(row_other, 1, Knight(color))
            self.squares(row_other)[6] = Square(row_other, 6, Knight(color))

        # Bishops -- 2
            self.squares(row_other)[2] = Square(row_other, 2, Bishop(color))
            self.squares(row_other)[5] = Square(row_other, 5, Bishop(color))

        # Rooks -- 2
            self.squares(row_other)[0] = Square(row_other, 0, Rook(color))
            self.squares(row_other)[7] = Square(row_other, 7, Rook(color))

        # Queen -- 1
            self.squares(row_other)[3] = Square(row_other, 3, Queen(color))

        # King -- 1
            self.squares(row_other)[4] = Square(row_other, 4, King(color))
