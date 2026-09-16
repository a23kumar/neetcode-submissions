# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        d1 = deque([p])
        d2 = deque([q])


        while d1 and d2:
            c1 = d1.popleft()
            c2 = d2.popleft()

            if c1 is None and c2 is None:
                continue
            
            if c1 is None or c2 is None or c1.val != c2.val:
                return False

            d1.append(c1.left)
            d2.append(c2.left)
            d1.append(c1.right)
            d2.append(c2.right)
        
        return True