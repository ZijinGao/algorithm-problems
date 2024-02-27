class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pointer = 0
        self.mapping = {}

    def helper(self, preorder, start, end):
        if start > end:
            return None
        val = preorder[self.pointer]
        root = TreeNode(val)
        
        self.pointer += 1
        root.left = self.helper(preorder, start, self.mapping[val] - 1)
        root.right = self.helper(preorder, self.mapping[val] + 1, end)
        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        for idx, val in enumerate(inorder):
            self.mapping[val] = idx        
        return self.helper(preorder, 0, len(preorder)-1)