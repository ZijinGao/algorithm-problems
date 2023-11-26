class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        n = len(piles)
        choice = piles[ n//3 :]
        out = 0
        for i in range(0, n // 3 * 2, 2):
            out += choice[i]
        return out