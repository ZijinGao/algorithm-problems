class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        result = []
        def backtrack(curr_str):
            if len(curr_str) == len(digits):
                result.append(curr_str)
                return
            next_digit = digits[len(curr_str)]
            for letter in mapping[next_digit]:
                backtrack(curr_str + letter)
        backtrack("")
        return result