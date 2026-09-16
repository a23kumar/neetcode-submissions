class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        multiplier = 1

        for i in range(len(digits) - 1, -1, -1):
            res += digits[i] * multiplier
            multiplier *= 10
        return list(str(res + 1))