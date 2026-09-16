class Solution:
    def isHappy(self, n: int) -> bool:
        # My original solution
        seen = set()

        while n != 1:
            digits = list(str(n))
            total = 0
            for num in digits:
                total += int(num) ** 2
            if total in seen:
                return False
            seen.add(total)
            n = total
        
        return True