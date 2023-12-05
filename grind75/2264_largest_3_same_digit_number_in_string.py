class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = []
        for idx, char in enumerate(num):
            if idx + 2 < len(num):
                if char == num[idx + 1] and char == num[idx + 2]:
                    l.append(num[idx: idx + 3])
        return max(l) if l else ''