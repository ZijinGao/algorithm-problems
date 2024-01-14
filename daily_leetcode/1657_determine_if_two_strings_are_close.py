from collections import defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        if len(set(word1)) != len(set(word2)):
            return False

        table1 = defaultdict(int)
        table2 = defaultdict(int)

        for c in word1:
            table1[c] += 1
        for c in word2:
            table2[c] += 1
            
        if sorted(list(table1.keys())) == sorted(list(table2.keys())) and sorted(list(table1.values())) == sorted(list(table2.values())):
            return True
        else:
            False