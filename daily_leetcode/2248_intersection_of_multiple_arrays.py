class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        res = set(nums[0])
        for i in range(1, len(nums)):
            res &= set(nums[i])
        return sorted(list(res))