### cannot use linkedlist, because can't randomly select item in O(1)
### from dictionary or linkedlist
### in other words, an array data structure is NEEDED,
### and I need to do optimization on top of array so that deletion is O(1)
import random
class RandomizedSet:
    def __init__(self):
        self.mapping = {} # {val: idx}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.mapping:
            return False

        self.array.append(val)
        self.mapping[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mapping:
            return False

        idx = self.mapping[val]
        last = self.array[-1]
        self.array[idx] = last
        self.array[-1] = val
        self.mapping[last] = idx

        self.array.pop()
        del self.mapping[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)