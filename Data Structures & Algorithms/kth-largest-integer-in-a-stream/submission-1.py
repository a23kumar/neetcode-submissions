class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
    def add(self, val: int) -> int:
        self.nums.append(val)
        heap_nums = [-s for s in self.nums]
        heapq.heapify(heap_nums)
        for _ in range(self.k - 1):
            heapq.heappop(heap_nums)
        return -heapq.heappop(heap_nums)

