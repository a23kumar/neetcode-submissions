class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) / 2
        dp = set()
        dp.add(0)
        # All we need is to find one subset where equal to target
        for i in range(n):
            temp_dp = dp.copy()
            for v in dp:
                if target in temp_dp:
                    return True
                temp_dp.add(v + nums[i])
            dp = temp_dp
        return target in dp