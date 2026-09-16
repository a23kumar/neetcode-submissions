class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_indx = len(matrix) * len(matrix[0])

        l , r = 0, num_indx - 1

        while l <= r:
            m = l + (r - l) // 2

            x,y = m // len(matrix[0]), m % len(matrix[0])

            if matrix[x][y] == target:
                return True
            
            if matrix[x][y] < target:
                l = m + 1
            else:
                r = m - 1
        return False