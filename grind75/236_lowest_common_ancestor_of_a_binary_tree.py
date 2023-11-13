# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        n = 0
        mapping = {} # {node.val: node}
        dp = {} # {node.val: [ancestor1.val (parent), ancestor2.val, ancestor4.val, ancestor8.val, ... ancestor2^i.val]}
        time = 0
        times = {} # {node.val: [in-time, out-time]}

        def _count_nodes(node):
            if not node:
                return
            # only n needs nonlocal because it is an integer. mapping and dp don't need one
            nonlocal n
            n += 1
            mapping[node.val] = node
            dp[node.val] = []

            _count_nodes(node.left)
            _count_nodes(node.right)

        def _dfs_build(node, prev):
            if not node:
                return 
            # same as above, time needs nonlocal here and times doesn't need one
            nonlocal time
            time += 1
            times[node.val] = [time, None]

            # current node processing logic
            dp[node.val][0] = prev.val
            for i in range(1, height):
                if dp[node.val][i - 1]:
                    dp[node.val][i] = dp[ dp[node.val][i - 1] ][i - 1]

            # recursive call
            _dfs_build(node.left, node)
            _dfs_build(node.right, node)

            times[node.val][1] = time

        def _is_ancestor(a: int, b: int) -> bool:
            if times[a][0] < times[b][0] and times[a][1] >= times[b][1]:
                return True
            return False

        def LCA(a, b):
            if _is_ancestor(a.val, b.val):
                return a
            elif _is_ancestor(b.val, a.val):
                return b
            else:
                for i in range(height-1, -1, -1):
                    if dp[a.val][i] != None and _is_ancestor(dp[a.val][i], b.val) == False:
                        a = mapping[dp[a.val][i]]

                return mapping[dp[a.val][0]]

        _count_nodes(root)
        height = math.ceil(math.log2(n))

        for node in dp.keys():
            dp[node] = [None for _ in range(height)]

        _dfs_build(root.left, root)
        _dfs_build(root.right, root)
        times[root.val] = [0, time]

        return LCA(p, q)