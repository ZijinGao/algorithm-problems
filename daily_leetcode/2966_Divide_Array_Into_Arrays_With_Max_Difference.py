class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        i = 0
        res = []
        while i <= len(nums) - 1:
            if nums[i+2] - nums[i+1] <= k and nums[i+1] - nums[i] <= k and nums[i+2] - nums[i] <= k: 
                res.append([nums[i], nums[i+1], nums[i+2]])
                i += 3
                continue
            else: 
                return []
        return res