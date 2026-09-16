# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = float("-inf")
        def dfs(node, max_seen):
            if not node:
                return 0
            res = 1 if node.val >= max_seen else 0
            max_seen = max(node.val, max_seen)
            res += dfs(node.left, max_seen)
            res += dfs(node.right, max_seen)
            
            return res
        return dfs(root, root.val)