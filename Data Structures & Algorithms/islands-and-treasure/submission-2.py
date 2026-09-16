from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # -1: water cell cant be traversed
        # 0: treasure chest
        # 3: inf - can be traversed -represented by 2147483647\
        
        ROW = len(grid)
        COL = len(grid[0])
        q = deque()
        visit = set()
        counter = 1

        # create a bfs method
        def bfs(i, j, grid):
            if i < 0 or j < 0 or i >= ROW or j >= COL or (i, j) in visit or grid[i][j] == -1:
                return
                
            grid[i][j] = counter
            visit.add((i, j))
            q.append((i, j))
        
        # load up a queue with all the treasure chests
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))

        # q = [(0, 2), (3, 0)]

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                bfs(i - 1, j, grid)
                bfs(i, j - 1, grid)
                bfs(i + 1, j, grid)
                bfs(i, j + 1, grid)
            counter += 1