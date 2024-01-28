class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1
        
        if m == 1 or n == 1:
            return 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]