from collections import Counter
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        table = Counter(nums)

        res = [None, None]
        for i in range(1, n+1):
            if i not in table:
                res[1] = i
            elif table[i] == 2:
                res[0] = i
            if res[0] and res[1]:
                break
        return res