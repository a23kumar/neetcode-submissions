class Solution:
    def isHappy(self, n: int) -> bool:
        seen = list()

        while n != 1:
            digits = list(str(n))
            total = 0
            for num in digits:
                total += int(num) ** 2
            if total in seen:
                return False
            seen.append(total)
            n = total
        
        return True