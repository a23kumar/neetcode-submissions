class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        elif len(nums) == 3:
            return max(nums)

        r1, r2, r3, r4 = 0, 0, 0, 0

        for i in range(len(nums) - 1):
            temp = max(nums[i] + r1, r2)
            r1 = r2
            r2 = temp

        x = max(r1, r2)
        for i in range(1, len(nums)):
            temp = max(nums[i] + r3, r4)
            r3 = r4
            r4 = temp
        y = max(r3, r4)
        
        return max(x, y)
