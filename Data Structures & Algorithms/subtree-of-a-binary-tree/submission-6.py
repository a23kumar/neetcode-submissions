# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        def dfs(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            if root.val != subroot.val:
                return False
            return dfs(root.left, subroot.left) and dfs(root.right, subroot.right)
        stack = [root]

        while stack:
            cur = stack.pop()

            if cur.val == subroot.val and dfs(cur, subroot):
                return True
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return False