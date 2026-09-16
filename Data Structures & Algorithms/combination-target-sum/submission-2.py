class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums are distinct
        # Return a list of all unique combinations that sum to target
        # Important: Same number from nums can be chosen an unlimited number of times
        # Combos are the same if frequency of each of the chosen numbers is the same
        res = []
        def dfs(i, subset, cur):
            if cur == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or cur > target:
                return

            #This is the section where we keep adding the same index in nums
            subset.append(nums[i])
            cur += nums[i]
            dfs(i, subset, cur)

            # Once we have exceeded 
            temp = subset.pop()
            cur -= temp
            dfs(i + 1, subset, cur)
        dfs(0, [], 0)
        return res
