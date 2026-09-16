class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = low + (high - low) // 2
            a = mid // n
            b = mid % n
            if target < matrix[a][b]:
                high = mid - 1
            elif target > matrix[a][b]:
                low = mid + 1
            else:
                return True
        return False