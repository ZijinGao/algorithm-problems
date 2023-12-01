from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        wordlength = len(beginWord)
        word_map = defaultdict(list)
        for word in wordList:
            for i in range(wordlength):
                word_map[word[:i] + "*" + word[i+1:]].append(word)
        visited = set()
        queue = deque([(beginWord, 1)])
        while queue:
            cur, level = queue.popleft()
            if cur == endWord:
                return level
            for i in range(wordlength):
                for word in word_map[cur[:i] + "*" + cur[i+1:]]:
                    if word not in visited:
                        queue.append([word, level + 1])
                        visited.add(word)
        return 0

# word_map
'''{ *ot : hot, dot, lot
    h*t : hot
    ho* :hot
    d*t : dot
    do* : dot, dog
    *og : dog, log, cog
    d*g : dog
    l*t : lot
    lo* : lot, log
    l*g : log
    c*g: cog
    co* : cog 
    }
'''

'''                              hit, level = 1
                            /            |              \
                    *it                h*t                  hi*
                    |                 |                     |     
                    null  	       hot ,level = 2      null
                                    /   |   \    
                                /    |     \
                        *ot           h*t      ho*
                    /    |   \         |        |
                hot,2   dot,3  lot,3   hot,2    hot,2	
'''