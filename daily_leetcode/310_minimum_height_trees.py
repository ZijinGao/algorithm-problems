import heapq
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1: return [0]

        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                connectedLeaf = adj[leaf].pop()
                adj[connectedLeaf].remove(leaf)
                if len(adj[connectedLeaf]) == 1:
                    newLeaves.append(connectedLeaf)
            leaves = newLeaves

        return leaves