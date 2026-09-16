class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #unique_array = []
        while nums:
            val = nums.pop(0)
            print(val)
            if val in nums:
               return True
            print(nums)
        return False