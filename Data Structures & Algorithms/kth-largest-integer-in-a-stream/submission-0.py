class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
    # use a heaps
    def add(self, val: int) -> int:
        self.nums.append(val)
        heap_nums = [-s for s in self.nums]
        heapq.heapify(heap_nums)
        print(heap_nums)
        for _ in range(self.k - 1):
            heapq.heappop(heap_nums)
        return -heapq.heappop(heap_nums)

        '''# first append the value to the array
        self.nums.append(val)
        # Then sort the numbers in ascending order
        self.nums.sort()
        temp = self.nums
        print(temp)
        # Iterate for k -1 number of times so that the kth value is at the top of the stack
        for _ in range(self.k - 1):
            temp.pop()
        return temp[-1]'''

