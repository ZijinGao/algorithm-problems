class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        occurance = {}
        res = []
        for num in nums:
            if num not in occurance:
                occurance[num] = 1
            else:
                res.append(num)

        return res   