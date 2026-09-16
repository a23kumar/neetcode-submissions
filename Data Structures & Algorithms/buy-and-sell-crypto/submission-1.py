class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        max_prof = 0

        p1 = 0
        p2 = 1

        while p2 <= (len(prices) - 1):
            if prices[p2] - prices[p1] < 0:
                p1 = p2
                p2 += 1
            else:
                max_prof = max(prices[p2] - prices[p1], max_prof)
                p2 += 1
        return max_prof