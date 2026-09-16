class Solution:
    def numDecodings(self, s: str) -> int:
        # A -> 1
        # B -> 2

        # JAB -> 1012 -> 10 1 2 -> 10 12
        # Constraints:
        # 1. No leading zeros for any segment
        # 2. Any segment must be between (inclusive) 1 -> 26
        # 3. Cannot map a zero

        # Prereqs
        # Can map a char to an in using ord

        # If there is a zero, need to check it val before is 1, or 2
        # Otherwise all values from that zero and become invalid 
        # and dp[i] becomes zero
        # If the value before is a 1 or 2, dp[i] = dp[i-1]
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, n + 1):
            prev = s[i-1]
            if prev != "0":
                dp[i] += dp[i-1]
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[n]
