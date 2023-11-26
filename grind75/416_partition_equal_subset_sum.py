## recursion with memoization
## equals to: not manually using memo and only using @cache

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        half = total // 2
        memo = [[None for j in range(total + 1)] for i in range(len(nums))]

        # @cache
        def dfs(idx, curr_sum):
            if idx == len(nums): # reaching the end and curr_combination is not half
                return False
            if curr_sum == half:
                return True
            if memo[idx][curr_sum] is not None:
                return memo[idx][curr_sum]
            result = dfs(idx + 1, curr_sum) or dfs(idx + 1, curr_sum + nums[idx])
            memo[idx][curr_sum] = result
            return result
        return dfs(0, 0)
    
## time complexity: O(m * n)