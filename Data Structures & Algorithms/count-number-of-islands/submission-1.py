class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Want to iterate through all vals in the array
        r = len(grid)
        c = len(grid[0])
        num_islands = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    # Run a dfs to look for vals in the island
                    self.dfs(grid, i, j)
                    num_islands += 1
        return num_islands

    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0" or grid[r][c] == "V":
            return
        
        grid[r][c] = "V"
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
