class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # We want to traverse through all the values in the grid
        ROW, COL = len(grid), len(grid[0])
        num_islands = 0
        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= ROW or j >= COL or grid[i][j] == "0" or grid[i][j] == "V":
                return

            grid[i][j] = "V" # set the land cell to visited

            dfs(i + 1, j, grid)
            dfs(i, j+1, grid)
            dfs(i - 1, j, grid)
            dfs(i, j - 1, grid)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    dfs(i, j, grid)
                    num_islands += 1
        return num_islands

