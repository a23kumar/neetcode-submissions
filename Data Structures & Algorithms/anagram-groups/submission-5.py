from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = defaultdict(list)
        res = []

        for s in strs:
            char_count = [0] * 26
            for c in s:
                i = ord(c) - ord("a")
                char_count[i] += 1
            mappings[tuple(char_count)].append(s)

        return list(mappings.values())
