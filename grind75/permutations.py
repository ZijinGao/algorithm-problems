class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # [1, 2, 3, 4]
        result = []
        n = len(nums)
        def permutation(curr_comb: list[int], visited: set[int]):
            if len(curr_comb) == n:
                result.append(curr_comb[:])
                return
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    curr_comb.append(num)
                    permutation(curr_comb, visited)
                    curr_comb.pop()
                    visited.remove(num)

        permutation([], set())
        return result