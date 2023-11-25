from collections import defaultdict
class UnionFind:
    def __init__(self, sz):
        self.root = []
        self.size = []

        for i in range(sz):
            self.root.append(i)
            self.size.append(1)

    def find(self, x):
        if x == self.root[x]: return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY: return

        if self.size[rootX] >= self.size[rootY]:
            self.size[rootX] += self.size[rootY]
            self.root[rootY] = rootX
        else:
            self.size[rootY] += self.size[rootX]
            self.root[rootX] = rootY

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # PREPROCESSING
        size = len(accounts)
        uf = UnionFind(size)
        emailGroup = {}

        # group emails by group id (0 ~ n-1)
        for i in range(size):
            emails = accounts[i][1:]
            for email in emails:
                if not emailGroup.get(email):
                    print(f"email: {email}")
                    print(f"emailGroup: {emailGroup}")
                # if email not in emailGroup:
                    emailGroup[email] = i
                else:
                    uf.union(i, emailGroup[email])

        groups = {}
        for email, group in emailGroup.items():
            groupRoot = uf.find(group)

            if groupRoot not in groups:
                groups[groupRoot] = []
            groups[groupRoot].append(email)
        
        out = []
        print(groups)
        for group, emails in groups.items():
            emails.sort()
            out.append([accounts[group][0]] + emails[:])
        return out
