class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]

        for i in range(2, len(cost)):
            o1 = cost[i] + first
            o2 = cost[i] + second

            cost[i] = min(o1, o2)
            first = cost[i - 1]
            second = cost[i]

        return min(first, second)