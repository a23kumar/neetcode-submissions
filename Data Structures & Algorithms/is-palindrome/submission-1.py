import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Case where len(s) is 1
        s = s.replace(" ", "").lower()
        s = re.sub(r'\W+', '', s)
        '''if len(s) == 1:
            return True'''

        p1 = 0
        p2 = len(s) - 1

        print(s)

        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True