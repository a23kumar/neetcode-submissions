class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        root = TrieNode()
        for word in wordDict:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.is_word = True

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            cur = root
            for j in range(i, n):
                c = s[j]
                if c not in cur.children:
                    break
                cur = cur.children[c]
                if cur.is_word:
                    dp[j+1] = True
        return dp[n]
