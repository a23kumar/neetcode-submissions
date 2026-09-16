class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        while nums:
            if len(nums) == 1:
                return heapq.heappop(nums)
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            if a != b:
                return a