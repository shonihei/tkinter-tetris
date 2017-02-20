import tkinter as tk
from board import *
import random as R

class app(tk.Frame):
    pieces = ["O","I","S","Z","L","J","T"]

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Hello")
        self.gameStarted = False
        self.boardState = Board(20, 10, 30)
        self.parent.bind("<KeyPress>", self.keydown)
        self.c = tk.Canvas(self.parent, width=400, height=600)
        self.initBoard()
        self.c.pack()


    def keydown(self, e):
        # space = 32
        # UP = 63232
        # DOWN = 63233
        # LEFT = 63234
        # RIGHT = 63235

        # Start game
        if ord(e.char) == 32:
            if not self.gameStarted:
                self.gameStarted = True



    def AddPiece(self):
        piece_index = R.randint(0, 6)
        self.boardState.add_piece(app.pieces[piece_index])
        self.boardState.moveCurDown()
        self.redrawBoard()

    def AutoMoveDown(self):
        self.redrawBoard()
        self.parent.after(2000, self.Gravity())

    def redrawBoard(self):
        for r in range(self.boardState.rows):
            for c in range(self.boardState.cols):
                piece = self.boardState.piece_at(r, c)
                self.c.itemconfig(self.tiles[r][c], fill=Board.colors[piece])

    def initBoard(self):
        size = self.boardState.square_width
        tiles = []
        for r in range(self.boardState.rows):
            row = []
            for c in range(self.boardState.cols):
                x1 = c * size
                y1 = r * size
                x2 = x1 + size
                y2 = y1 + size
                piece = self.boardState.piece_at(r, c)
                row.append(self.c.create_rectangle(x1,y1,x2,y2, fill=Board.colors[piece]))
            tiles.append(row)
        self.tiles = tiles

if __name__ == "__main__":
    root = tk.Tk()
    app(root).pack()
    root.mainloop()
