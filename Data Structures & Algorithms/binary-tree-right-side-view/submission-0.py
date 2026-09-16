# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qlen = len(q)
            for i in range(qlen):
                curr = q.popleft()
                if curr:
                    rightSide = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if rightSide:
                res.append(rightSide.val)
        return res            