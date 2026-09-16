class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for indx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stackVal, stackInd = stack.pop()
                result[stackInd] = (indx - stackInd)
            stack.append((val, indx))
        return result