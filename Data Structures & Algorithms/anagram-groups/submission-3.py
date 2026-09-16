from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hm to heep track of all anagrams
        hm = defaultdict(list)
        # Loop through all strings in the list
        for val in strs:
            print(val)
            # Create a print for each val
            stamp = [0] * 26
            # loop through all chars in each val
            for char in val:
                # we can determine the appropriate index to increment by 
                # by using ord()
                indx = ord(char) - ord('a')
                stamp[indx] += 1
            arr = tuple(stamp)
            hm[arr].append(val)
        return list(hm.values())
