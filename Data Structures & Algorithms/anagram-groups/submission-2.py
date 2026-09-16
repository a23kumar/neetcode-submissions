class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            freq = [0] * 26

            for l in s:
                indx = ord(l) - ord('a')
                freq[indx] += 1
            hm[tuple(freq)].append(s)
        return hm.values()