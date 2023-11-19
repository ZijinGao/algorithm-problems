from collections import defaultdict
from random import choice
class RandomizedCollection:
    def __init__(self):
        self.mapping = defaultdict(set)
        self.array = []

    def insert(self, val: int) -> bool:
        out = True
        if self.mapping[val]:
            out = False
        self.mapping[val].add(len(self.array))
        self.array.append(val)
        return out

    def remove(self, val: int) -> bool:
        if not self.mapping[val]: return False

        curr_idx = self.mapping[val].pop()
        last_val = self.array[-1]
        self.array[curr_idx] = last_val
        last_idx = len(self.array) - 1
        
        # order matters for edge case where the last ono is the one to be deleted !!!
        self.mapping[last_val].add(curr_idx)
        self.mapping[last_val].remove(last_idx)
        
        self.array.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.array)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()