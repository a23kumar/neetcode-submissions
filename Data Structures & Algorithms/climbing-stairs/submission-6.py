class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        p2 = 1
        p1 = 2
        cur = None
        # p2 = 1
        # p1 = 2
        # cur = 3
        for i in range(3, n + 1):
            cur = p1 + p2
            p2 = p1
            p1 = cur
            cur = None
        return p1