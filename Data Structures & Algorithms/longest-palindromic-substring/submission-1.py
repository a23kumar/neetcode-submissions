class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_index = 0
        res_len = 0
        
        for i in range(len(s)):

            # Even case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > res_len:
                    res_index = l
                    res_len = length
                l -= 1
                r += 1
            # Odd case
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
               length = r - l + 1
               if length > res_len:
                   res_index = l
                   res_len = length
               l -= 1
               r += 1
        return s[res_index:res_index + res_len]