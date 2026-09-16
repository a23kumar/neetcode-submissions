class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''if len(s) == 0:
            return 0'''
        p1 = 0
        sett = set()
        largest = 0
        for p2, val in enumerate(s):
            while s[p2] in sett:
                largest = max(len(sett), largest)
                sett.remove(s[p1])
                p1 += 1
            sett.add(val)
        return max(len(sett), largest)


