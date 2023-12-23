class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeros_from_left = [0 for i in range(n-1)]
        ones_from_right = [0 for i in range(n-1)]

        count_0 = 0
        for i in range(n-1):
            if s[i] == "0":
                count_0 += 1
            zeros_from_left[i] = count_0
        
        count_1 = 0
        for i in range(n-1, 0, -1):
            if s[i] == "1":
                count_1 += 1
            ones_from_right[i-1] = count_1
        # ones_from_right[0] = ones_from_right[1] ## added
        
        max_val = float('-inf')
        for i in range(n-1):
            max_val = max(max_val, zeros_from_left[i] + ones_from_right[i])
        
        return max_val