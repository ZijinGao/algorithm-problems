class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positives = []
        negatives = []
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        res = []
        for i in range(len(positives)):
            res.append(positives[i])
            res.append(negatives[i])
        return res