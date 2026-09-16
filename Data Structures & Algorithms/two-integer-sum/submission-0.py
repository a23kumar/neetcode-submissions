class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = []
        for i, j in enumerate(nums):
            val = target - j
            if val in nums[i+1:]:
                idx.append(i)
                idx.append(nums.index(val, i+1))
        return idx