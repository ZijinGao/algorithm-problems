# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = -1

        def dfs(node, max_in_path, min_in_path):
            if not node:
                return
            nonlocal max_diff
            max_in_path = max(max_in_path, node.val)
            min_in_path = min(min_in_path, node.val)
            max_diff = max(max_diff, max_in_path - min_in_path)
            dfs(node.left, max_in_path, min_in_path)
            dfs(node.right, max_in_path, min_in_path)
        
        dfs(root, float('-inf'), float('inf'))
        return max_diff