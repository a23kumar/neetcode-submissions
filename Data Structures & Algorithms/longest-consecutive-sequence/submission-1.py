class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert the list into a hashtable
        # this removes duplicates and allows for O(1) lookup times
        set_nums = set(nums)

        # keep a master tracker for longest consecutive sequence
        longest = 0
        
        
        for n in nums:
            if n - 1 not in set_nums:
                length = 0
                while n + length in set_nums:
                    length += 1
                longest = max(length, longest)
        return longest