class Solution:
    def rob(self, nums: List[int]) -> int:
        #buttom up approach
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        r1, r2 = 0, 0
        for i in range(len(nums)):
            temp = max(r2, nums[i] + r1)
            r1 = r2
            r2 = temp
        return r2
        
        
