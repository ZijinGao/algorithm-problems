class TrieNode:
    def __init__(self, name):
        self.map = {}
        self.name = name
        self.value = -1

class FileSystem:
    def __init__(self):
        self.root = TrieNode("")

    def createPath(self, path: str, value: int) -> bool:
        if path == '/' or len(path) == 0:
            return False

        components = path.split('/')
        cur = self.root
        for idx, path in enumerate(components):
            if idx == 0: continue
            if idx == len(components) - 1:
                if path in cur.map and cur.map[path].value != -1: # already exists
                    return False
                node = TrieNode(path)
                node.value = value
                cur.map[path] = node
                return True
            elif path not in cur.map:
                return False
            else:
                cur = cur.map[path]

    def get(self, path: str) -> int:
        components = path.split('/')
        cur = self.root
        for idx, path in enumerate(components):
            if idx == 0: continue
            if path not in cur.map:
                return -1
            cur = cur.map[path]
        return cur.value