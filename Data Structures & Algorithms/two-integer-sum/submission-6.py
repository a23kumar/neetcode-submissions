class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = dict()

        for i, j in enumerate(nums):
            diff = target - j
            if diff in hm:
                return [hm[diff], i]
            hm[j] = i