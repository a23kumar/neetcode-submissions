class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, curr, curr_total):
            if curr_total == target:
                res.append(curr[:])
                return
            if i >= len(nums) or curr_total > target:
                return

            curr.append(nums[i])
            dfs(i, curr, curr_total + nums[i])

            curr.pop()
            dfs(i + 1, curr, curr_total)

        dfs(0, curr, 0)
        return res