class Node:
    def __init__(self, value, nextNode=None):
        self.val = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        self.head = Node(-1)

    def insert(self, val):
        if not self.exists(val):
            newNode = Node(val, self.head.next)
            self.head.next = newNode
    
    def exists(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    def delete(self, val):
        if not self.exists(val): return
        curr = self.head
        prev = curr
        while curr:
            if curr.val == val:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

class MyHashSet:
    def __init__(self):
        self.hash_space = 1297
        self.hashset = [Bucket() for _ in range(self.hash_space)]

    def add(self, key: int) -> None:
        idx = key % self.hash_space
        self.hashset[idx].insert(key)

    def remove(self, key: int) -> None:
        idx = key % self.hash_space
        self.hashset[idx].delete(key)

    def contains(self, key: int) -> bool:
        idx = key % self.hash_space
        return self.hashset[idx].exists(key)