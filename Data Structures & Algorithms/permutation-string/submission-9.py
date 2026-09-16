class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        l = 0
        r = 0
        for v in s1:
            s1_freq[ord(v) - ord('a')] += 1
        print(s1_freq)
        while r < (len(s2)):
            
            s2_freq[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) > len(s1):
                s2_freq[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if s1_freq == s2_freq:
                return True
            r += 1
            print(s2_freq)
        return False