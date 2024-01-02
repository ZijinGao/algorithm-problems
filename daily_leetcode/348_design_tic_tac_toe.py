class TicTacToe:
    def __init__(self, n: int):
        self.p1_scores = [0 for i in range(2 * n + 2)] # n: rows; n: n cols; 1: diag
        self.p2_scores = [0 for i in range(2 * n + 2)] # n: rows; n: n cols; 1: diag
        self.p1steps = 0
        self.p2steps = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.p1steps += 1
            self.p1_scores[row] += 1
            self.p1_scores[col + self.n] += 1
            if row == col:
                self.p1_scores[-1] += 1
            if row + col == self.n-1:
                self.p1_scores[-2] += 1
            if self.p1steps >= self.n and max(self.p1_scores) == self.n:
                    return 1
            else: return 0
        else:
            self.p2steps += 1
            self.p2_scores[row] += 1
            self.p2_scores[col + self.n] += 1
            if row == col:
                self.p2_scores[-1] += 1
            if row + col == self.n - 1:
                self.p2_scores[-2] += 1
            if self.p2steps >= self.n and max(self.p2_scores) == self.n:
                    return 2
            else: return 0