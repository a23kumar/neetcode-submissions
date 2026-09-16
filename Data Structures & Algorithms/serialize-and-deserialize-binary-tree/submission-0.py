from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root):
        if not root:
            return ""
        res = ""
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur:
                res += str(cur.val) + ","
                q.append(cur.left)
                q.append(cur.right)
            else:
                res += "N,"
        return res[:-1]

    # Decodes your encoded data to tree.
    def deserialize(self, data):
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            cur = q.popleft()
            if nodes[i] != "N":
                cur.left = TreeNode(int(nodes[i]))
                q.append(cur.left)
            i += 1
            if nodes[i] != "N":
                cur.right = TreeNode(int(nodes[i]))
                q.append(cur.right)
            i += 1
        return root
