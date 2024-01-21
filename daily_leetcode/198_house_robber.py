class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        for i in range(1, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]) 

        return dp[-1]