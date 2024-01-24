# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0
        def backtrack(table, node):
            # leaf node
            if not (node.left or node.right):
                odd_count = 0
                for key, value in table.items():
                    if value % 2 == 1:
                        odd_count += 1
                if odd_count <= 1:
                    nonlocal res
                    res += 1
                return
            
            # internal node
            if node.left:
                table[node.left.val] += 1
                backtrack(table, node.left)
                table[node.left.val] -= 1
            if node.right:
                table[node.right.val] += 1
                backtrack(table, node.right)
                table[node.right.val] -= 1

        table = defaultdict(int)
        table[root.val] += 1
        backtrack(table, root)
        return res
