# bottom-up dp
class Solution:
    def wordBreak(self, s: str, words: list[str]) -> bool:
        dp = [False for _ in range(len(s))]        
        for i in range(len(s)):
            for word in words:
                if i < len(word)-1:
                    continue
                elif i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1: i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]
    

# # recursion with memo
# class Solution:
#     def wordBreak(self, s: str, words: list[str]) -> bool:
#         length = len(s)
#         @cache
#         def dfs(idx):
#             if idx == length:
#                 return True
#             result = False
#             for word in words:
#                 if word == s[idx: idx + len(word)]:
#                     temp = dfs(idx + len(word))
#                     if temp:
#                         result = True
#             return result
#         return dfs(0)