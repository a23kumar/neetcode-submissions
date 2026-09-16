class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0]) - 1
        print(matrix[0][0], matrix[0][len(matrix[0]) - 1])
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][len(matrix[i]) - 1]:
                for val in matrix[i]:
                    print(val)
                    if val == target:
                        return True
                return False
        return False