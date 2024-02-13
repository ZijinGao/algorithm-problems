class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        def isPalindrome(word: str) -> bool:
            n = len(word)
            if n == 1: return True
            else:
                left = 0
                right = n - 1
                while left < right:
                    if word[left] == word[right]:
                        left += 1
                        right -= 1
                    else: return False
                if word[left] == word[right]:
                    return True
                else:
                    return False
        res = ""
        for word in words:
            if isPalindrome(word):
                return word
        return res