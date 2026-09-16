class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''if not stones:
            return 0

        if len(stones) == 1:
            return stones[0]
        
        idx1, max1 = max(stones)
        idx2, max2 = max(stones)
        stones.pop(max1)
        stones.pop(max2)
        if max1 == max2:
            continue
        elif max1 < max2:


        self.lastStoneWeight(stones)'''

        while stones and len(stones) > 1:
            v1 = max(stones)
            stones.remove(v1)
            v2 = max(stones)
            stones.remove(v2)

            if v1 == v2:
                continue

            elif v1 < v2:
                stones.append(v2 - v1)
            
            else:
                stones.append(v1 - v2)

        if not stones:
            return 0
        else:
            return stones[0]

