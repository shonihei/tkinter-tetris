class Board:
    pieces = {
        "O": [(0, 0), (0, -1), (-1, 0), (-1, -1)],
        "I": [(-2, 0), (-1, 0), (0, 0), (1, 0)],
        "S": [(0, 0), (1, 0), (0, -1), (-1, -1)],
        "Z": [(-1, 0), (0, 0), (0, -1), (1, -1)],
        "L": [(-1, 0), (-1, -1), (0, 0), (1, 0)],
        "J": [(-1, 0), (0, 0), (1, 0), (1, -1)],
        "T": [(-1, 0), (0, -1,), (0, 0), (1, 0)]
    }

    colors = {
        " ": "grey",
        "O": "yellow",
        "I": "cyan",
        "S": "red",
        "Z": "green",
        "L": "orange",
        "J": "pink",
        "T": "purple"
    }

    def __init__(self, numRows, numCols, sqwidth):
        self.board = [[" " for i in range(numCols)] for j in range(numRows)]
        self.rows = numRows
        self.cols = numCols
        self.centerCol = self.cols // 2 - 1
        self.square_width = sqwidth
        self.__bufferEmpty = True

    def __repr__(self):
        s = ""
        for i in range(self.rows):
            s += "|"
            for j in range(self.cols):
                s += str(self.board[i][j]) + "|"
            s += "\n"
        return s

    def add_piece(self, piece):
        piece_schematic = Board.pieces[piece]
        for coordinate in piece_schematic:
            self.board[0-coordinate[1]][self.centerCol-coordinate[0]] = piece

    def piece_at(self, row, col):
        return self.board[row][col]

def main():
    b = Board(20, 10, 10)
    #print(b)
    b.add_piece("O")
    print(b)

if __name__ == "__main__":
    main()
