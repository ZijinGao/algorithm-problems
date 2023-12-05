from collections import defaultdict
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        length = 0
        mapping = defaultdict(int)
        for char in chars:
            mapping[char] += 1
        
        for word in words:
            char_count = defaultdict(int)
            for char in word:
                char_count[char] += 1

            good = True
            for char, count in char_count.items():
                if count > mapping[char]:
                    good = False
                    break
            if good:
                length += len(word)
                
        return length
