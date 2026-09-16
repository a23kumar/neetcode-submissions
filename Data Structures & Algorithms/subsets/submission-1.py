class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def backtrack_dfs(i):
            # Base case, if index is >= len(nums)
            if i >= len(nums):
                res.append(subset[:])
                return
            
            # Decision to include nums[i]
            subset.append(nums[i])
            backtrack_dfs(i + 1)

            subset.pop()
            backtrack_dfs(i + 1)
        
        backtrack_dfs(0)
        return res
