# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            l = len(queue)
            rightmostnode = None
            for i in range(l):
                node = queue.popleft()
                rightmostnode = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(rightmostnode.val)
        return res