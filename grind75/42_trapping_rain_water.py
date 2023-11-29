class Solution:
    def trap(self, height: list[int]) -> int:
        max_from_left = [0 for _ in range(len(height))]
        max_from_right = [0 for _ in range(len(height))]

        if len(height) <= 2:
            return 0

        max_from_left[0] = height[0]
        max_from_right[-1] = height[-1]

        for i in range(1, len(height)):
            max_from_left[i] = max(max_from_left[i - 1], height[i])
        
        for i in range(len(height) - 2, -1, -1):
            max_from_right[i] = max(max_from_right[i + 1], height[i])
        
        out = 0

        for i in range(len(height)):
            out += min(max_from_left[i], max_from_right[i]) - height[i]
        return out