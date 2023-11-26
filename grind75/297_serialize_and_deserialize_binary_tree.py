# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        out = ''
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node:
                out += ",#"
            else:
                out += ","
                out += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
        out = out[1:]
        return out
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(nodes[0])
        queue = deque()
        queue.append(root)
        i = 1
        while i < len(nodes):
            node = queue.popleft()
            if nodes[i] != "#":
                left = TreeNode(nodes[i])
                node.left = left
                queue.append(left)
            i += 1
            if nodes[i] != "#":
                right = TreeNode(nodes[i])
                node.right =right
                queue.append(right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))