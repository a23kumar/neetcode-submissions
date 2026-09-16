class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min, cur_max = 1, 1
        res = nums[0]
        for n in nums:
            # What is the greatest out of the following options
            # 1. Just n
            # 2. The current min*n
            # 2. The current max*n
            temp = cur_max * n
            cur_max = max(n, cur_min * n, temp)
            cur_min = min(n, cur_min * n, temp)
            res = max(res, cur_max)
        return res

