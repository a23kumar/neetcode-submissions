# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []

        while q:
            right_side = None
            qlen = len(q)
            for i in range(qlen):
                cur = q.popleft()
                if cur:
                    right_side = cur.val
                    print(right_side)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            res.append(right_side)

        return res