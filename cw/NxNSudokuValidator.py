import numpy as np


class Sudoku(object):
    def __init__(self, data):
        self.data = data
        print(self.data)

    def is_valid(self):
        n = len(self.data[0])
        b = int(n ** 0.5)
        if (
            len(self.data) != n
            or any(len(i) != n for i in self.data)
            or any(i not in [1, 2, 3, 4, 5, 6, 7, 8, 9] for i in self.data)
        ):
            return False
        board = np.array(self.data, dtype=np.uint8)
        for row in board:
            if len(np.unique(row)) != n:
                return False
        for col in board.T:
            if len(np.unique(col)) != n:
                return False
        for i in range(b):
            for j in range(b):
                if len(np.unique(board[b * i : b * (i + 1), b * j : b * (j + 1)])) != n:
                    return False
        return True

