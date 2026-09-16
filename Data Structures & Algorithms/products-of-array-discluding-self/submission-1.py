class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize a res array. This is not included in memory
        res = [1] * len(nums) # 

        # Prefix and postfix pointer
        prefix = 1 # O(1)
        postfix = 1 # O(1)

        # iterate through all values getting their prefix values
        for i in range(len(nums)): # O(n)
            if i != 0:
                prefix *= nums[i - 1]
            res[i] = prefix
        # iterate through all values in revese getting their postfix values
        # and multiplying them in the curr index
        for i in range(len(nums) - 1, -1, -1): # O(n)
            if i != len(nums) - 1:
                postfix *= nums[i + 1]
            res[i] *= postfix
        
        # return res
        return res
        # Final time and space complexities
        # 2 * O(n) = O(n) time complexity
        # O(1) space complexity
            
