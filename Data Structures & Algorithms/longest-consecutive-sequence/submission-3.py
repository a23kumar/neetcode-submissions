class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        '''
        A sequence of consective numbers always has a start and a end
        A start of a sequence can be fond if a value does not have a prev value

        The end of the sequence can be found if the next consecutive number does not exist
        '''

        nums_set = set(nums)
        print(nums_set)
        
        max_len = 0
        for n in nums:
            if n - 1 not in nums_set:
                length = 1
                while n + length in nums_set:
                    length += 1
                if length > max_len:
                    max_len = length
        return max_len