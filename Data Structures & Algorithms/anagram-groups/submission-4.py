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

        for m in mappings:
            temp = []
            for s in mappings[m]:
                temp.append(s)
            res.append(temp)
        return res
