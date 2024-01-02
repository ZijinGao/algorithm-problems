from collections import defaultdict
class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        out = []
        count = defaultdict(int)
        if len(set(nums)) == len(nums):
            out.append(nums)
            return out

        for num in nums:
            count[num] += 1
        max_count = max(list(count.values()))
        while max_count > 0:
            temp = []
            for num, cnt in count.items():
                if cnt > 0:
                    temp.append(num)
                    count[num] -= 1
            out.append(temp)
            max_count -= 1
        return out
        

        