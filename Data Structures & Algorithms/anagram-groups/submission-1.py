from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a default dict that initializes all values as lists
        anagrams = defaultdict(list)
        # iterate through all values in the array
        for s in strs:
            # Initialize a running array counter where each index corresponds to a letter in the alphabet
            count = [0] * 26
            # iterate through all letters in each value
            for val in s:
                # convert to numbers and subtract from base a
                count[ord(val) - ord("a")] += 1
            # append to value with the key that corresponds to the count array
            # Due to the datatypes that can be stored as a key in a dict, we must turn this into a tuple
            anagrams[tuple(count)].append(s)
        # return all the values in the dictionary
        return anagrams.values()