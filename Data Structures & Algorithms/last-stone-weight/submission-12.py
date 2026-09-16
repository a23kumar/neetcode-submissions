class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # O(nlogn) solution with space complexity of O(n)
        stones = [-s for s in stones]
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            v1 = abs(heapq.heappop(stones))
            v2 = abs(heapq.heappop(stones))
            if v2 < v1:
                heapq.heappush(stones, v2 - v1)

        if not stones:
            return 0
        else:
            return abs(stones[0])

        # O(n^2) solution with O(1) Time complexity
        '''while stones and len(stones) > 1:
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
            return stones[0]'''