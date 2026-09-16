# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            len_level = len(q)
            level = []
            for i in range(len_level):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            if level:
                res.append(level)
        return res
            
        