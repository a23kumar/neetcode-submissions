class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        dict_t = defaultdict(int)
        dict_s = defaultdict(int)
        for l in t:
            dict_t[l] += 1
        target = len(dict_t)
        curr = 0
        l = 0
        res = ""
        res_len = float('inf')
        for r in range(len(s)):
            val = s[r]
            if val in dict_t:
                if (dict_s[val] + 1) == dict_t[val]:
                    curr += 1
                dict_s[val] += 1
            while curr == target:
                if len(s[l:r]) < res_len:
                    res_len = len(s[l:r])
                    res = s[l:r + 1] 
                if s[l] in dict_t:
                    dict_s[s[l]] -= 1
                    if dict_s[s[l]] < dict_t[s[l]]:
                        curr -= 1
                l += 1
        return res

                    
            

