class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        lowest = r
        while l <= r:
            m = (l + r) // 2
            local_count = 0
            for p in piles:
                local_count += math.ceil(p / m) 
            if local_count <= h:
                lowest = m
                r = m - 1
            else:
                l = m + 1        
        return lowest
