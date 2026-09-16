class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            local_max = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = local_max
        return rob2