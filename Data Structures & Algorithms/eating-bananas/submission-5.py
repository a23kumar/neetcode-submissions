class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #H: number of hours to eat all the bananas

        # 9//4 = 2
        # max(piles) / 2 = outut
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            time = 0
            for p in piles:
                time += (p + k - 1) // k
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
