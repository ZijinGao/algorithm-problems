class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[0][i] = matrix[0][i]

        for row in range(1, n):
            for col in range(n):
                if col - 1 >= 0:
                    dp[row][col] = min(dp[row][col], dp[row-1][col-1] + matrix[row][col])
                dp[row][col] = min(dp[row][col], dp[row-1][col] + matrix[row][col])
                if col + 1 < n:
                    dp[row][col] = min(dp[row][col], dp[row-1][col+1] + matrix[row][col])

        return min(dp[-1])