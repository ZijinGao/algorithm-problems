import bisect

# greedy with binary search
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sub = []
        for num in nums:
            if len(sub) == 0 or sub[-1] < num:
                sub.append(num)
            else:
                idx = bisect.bisect_left(sub, num)
                sub[idx] = num
        return len(sub)


# # n squared dp solution
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # dp[i] is the longest increasing subsequence that ends at nums[i]
#         dp = [1 for _ in (nums)]
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i] and dp[i] < dp[j] + 1:
#                     dp[i] = dp[j] + 1
#         return max(dp)