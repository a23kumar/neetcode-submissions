class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i + 1 == n:
                print('thing')
                continue
            
            if n == nums[n - 1]:
                print('thing1')
                return n
            else:
                print('thing2')
                temp = nums[n - 1]
                nums[n - 1] = n
                nums[i] = temp