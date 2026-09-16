class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for indx, num in enumerate(nums):
            lookup = target - num
            if lookup in hm:
                return [hm[lookup], indx]
            hm[num] = indx

        # {
        #     3: 0,
        #     4: 1,
        #     5: 2,
        #     6: 3
        # }
        