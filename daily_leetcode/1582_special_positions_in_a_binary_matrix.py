from collections import defaultdict

class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        memo_rows = defaultdict(set)
        memo_cols = defaultdict(set)
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    memo_rows[i].add((i, j))
                    memo_cols[j].add((i, j))
        set_rows = set()
        set_cols = set()
        for key, n in memo_rows.items():
            if len(n) == 1:
                set_rows.update(n)
        for key, n in memo_cols.items():
            if len(n) == 1:
                set_cols.update(n)
        return len(set_rows.intersection(set_cols))
        
        