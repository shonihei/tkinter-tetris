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

    def __init__(self, numRows, numCols, sqwidth):
        """
            First four rows act as a buffer and is not meant to be rendered
        """
        self.board = [[0 for i in range(numCols)] for j in range(numRows)]
        self.rows = numRows
        self.cols = numCols
        self.square_width = sqwidth
        self.__bufferEmpty = True

    def __repr__(self):
        s = ""
        for i in range(self.rows):
            for j in range(self.cols):
                s += str(self.board[i][j])
            s += "\n"
        return s

    def add_piece(self, piece):
        piece_schematic = Board.pieces[piece]
        centerCol = self.cols // 2
        for coordinate in piece_schematic:
            self.board[0][centerCol]
def main():
    b = Board(20, 10, 10)
    print(b)

if __name__ == "__main__":
    main()
