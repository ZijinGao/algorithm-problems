## bottom up solution 
class Solution1:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n * k < target:
            return 0
        MOD = 10**9 + 7
        dp = [[0 for col in range(target+1)] for row in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(i, min(i*k, target)+1):
                for mid in range(1, min(k,j)+1):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-mid]) % MOD

        return int(dp[-1][-1])
    

## top-down recursion with memo
## optimized it to work! >:)
class Solution2:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n * k < target:
            return 0

        @cache
        def backtrack(idx, curr_sum):
            if curr_sum > target:
                return 0
            elif curr_sum == target:
                if idx == n-1:
                    return 1
                return 0
            elif idx >= n: # 0 ~ n-1
                return 0
            else:
                out = 0
                for i in range(1, k+1):
                    out += backtrack(idx + 1, curr_sum + i)
                return out
        return backtrack(-1, 0) % (10**9 + 7)