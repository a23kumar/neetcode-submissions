# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # All node values are unique
        # Ancestor is allowed to be a decendant of itself
        
        # If cur.val == q.val or cur.val == p.val:
            # return cur.val
        # if q.val < cur.val < p.val or p.val < cur.val < q.val:
            # return cur.val
        # if p.val < cur.val and q.val < cur.val:
            # dfs(cur.left)
        # if p.val > cur.val and q.val > cur.val:
            # dfs(cur.right)
        def dfs(cur, p, q):
            if not cur:
                return None
            if p.val < cur.val and q.val < cur.val:
                return dfs(cur.left, p, q)
            elif p.val > cur.val and q.val > cur.val:
                return dfs(cur.right, p, q)
            else:
                return cur

        return dfs(root, p, q)

        