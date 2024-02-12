from collections import defaultdict
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        half = len(nums) / 2
        table = defaultdict(int)
        for num in nums:
            table[num] += 1
            if table[num] > half:
                return num