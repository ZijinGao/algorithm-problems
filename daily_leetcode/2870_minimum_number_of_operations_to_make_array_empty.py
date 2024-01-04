from collections import defaultdict
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1
        
        count = 0
        for val in mapping.values():
            if val < 2:
                return -1
            if val % 3 == 0:
                count += int(val // 3)
            else :
                count += val // 3 + 1
        return count