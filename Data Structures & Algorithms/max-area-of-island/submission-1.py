class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Questions:
        if len(grid[0]) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])
        max_area = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    max_area = max(max_area, area)

        return max_area

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        
        grid[i][j] = 9
        area = 1
        area += self.dfs(grid, i+1, j)
        area += self.dfs(grid, i, j+1)
        area += self.dfs(grid, i-1, j)
        area += self.dfs(grid, i, j-1)

        return area

