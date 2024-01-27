class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        for num in nums:
            l = len(res)
            for i in range(l):
                new = res[i][:]
                new.append(num)
                res.append(new)
        return res