# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. 
# Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        right = max(piles)
        left = math.ceil(sum(piles) / h)
        while left < right:
            mid = left + (right - left) // 2
            hours = sum([ math.ceil(count/mid) for count in piles])
            if hours <= h: # too fast
                right = mid
            else:
                left = mid + 1
        return left