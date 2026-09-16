import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, [dist, [x, y]])
        for _ in range(k):
            coord = heapq.heappop(heap)[1]
            res.append(coord)
        
        return res
