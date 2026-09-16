class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        '''dp = [0] * n

        dp[0], dp[1] = 1, 2'''

        x,y = 1, 2

        for i in range(2, n):
            temp = x + y
            x = y
            y = temp
        return y