import tkinter as tk
from board import *
import random as R

class app(tk.Frame):
    pieces = ["O","I","S","Z","L","J","T"]

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Hello")
        self.tiles = {}
        self.gameStarted = False
        self.boardState = Board(20, 10, 30)
        self.parent.bind("<KeyPress>", self.keydown)
        self.c = tk.Canvas(self.parent, width=400, height=600)
        self.drawBoard(self.c)
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
                piece_index = R.randint(0, 6)
                self.boardState.add_piece(app.pieces[piece_index])
                self.gameStarted = True
                self.drawBoard(self.c)
        else:
            pass

    def drawBoard(self, canvas):
        size = self.boardState.square_width
        for r in range(self.boardState.rows):
            for c in range(self.boardState.cols):
                x1 = c * size
                y1 = r * size
                x2 = x1 + size
                y2 = y1 + size
                piece = self.boardState.piece_at(r, c)
                tile = canvas.create_rectangle(x1,y1,x2,y2, fill=Board.colors[piece])
                self.tiles[r,c] = tile

if __name__ == "__main__":
    root = tk.Tk()
    app(root).pack()
    root.mainloop()
