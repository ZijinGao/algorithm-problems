class Solution:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        n = len(candidates)

        def helper(curr_sum: int, combination: list[int], curr_idx: int):
            if curr_sum > target:
                return
            elif curr_sum == target:
                result.append(combination[:])
                return
            else:
                for i in range(curr_idx, n):
                    combination.append(candidates[i])
                    helper(curr_sum + candidates[i], combination, i)
                    combination.pop()

        helper(0, [], 0)
        return result