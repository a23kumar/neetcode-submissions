class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        res = []
        for n in nums:
            heapq.heappush(heap, -n)
        
        cnt = 0
        while cnt < k:
            cnt += 1
            res = -1 * heapq.heappop(heap)

        return res

        
