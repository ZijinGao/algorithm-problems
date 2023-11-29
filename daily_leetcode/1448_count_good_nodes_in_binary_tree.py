class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, max_on_path):
            if not node:
                return
            if max_on_path <= node.val:
                nonlocal count
                count += 1
            max_on_path = max(max_on_path, node.val)
            dfs(node.left, max_on_path)
            dfs(node.right, max_on_path)

        dfs(root, float('-inf'))
        return count