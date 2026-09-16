class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        multiplier = 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits