class Bucket:
    def __init__(self):
        self.bucket = []
    
    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for idx, (k, v) in enumerate(self.bucket):
            if k == key:
                self.bucket[idx] = (key, value)
                found = True
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for (k, v) in self.bucket:
            if k == key:
                self.bucket.remove((k, v))

class MyHashMap:
    def __init__(self):
        self.key_space = 1197
        self.hash_table = [Bucket() for _ in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.key_space
        self.hash_table[idx].update(key, value)

    def get(self, key: int) -> int:
        idx = key % self.key_space
        return self.hash_table[idx].get(key)

    def remove(self, key: int) -> None:
        idx = key % self.key_space
        self.hash_table[idx].remove(key)