from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we can first do a pass to find the treasure chests
        self.cycles = 0
        ROW = len(grid)
        COL = len(grid[0])
        q = deque()
        visit = set()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    visit.add((i, j))
                    q.append([i, j])
        
        def addCell(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == -1 or (i, j) in visit:
                return

            visit.add((i, j))
            q.append([i, j])

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = self.cycles
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            self.cycles += 1
