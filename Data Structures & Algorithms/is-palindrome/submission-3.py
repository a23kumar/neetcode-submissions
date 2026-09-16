import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach
        s = s.replace(" ", "").lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        p1 = 0
        p2 = len(s) - 1
        print(s)
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 +=1 
            p2 -= 1
        return True
