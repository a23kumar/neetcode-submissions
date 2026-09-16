class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Each cell can have have
        # 0 - Empty cell
        # 1 - reps fresh fruit
        # 2 - reps rotten fruit
        ROW, COL = len(grid), len(grid[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        elapsed_time = 0
        fresh_fruit = 0
        q = deque()
        # First we want to know how many fresh fruit there are and where the rotten ones are
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh_fruit += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        while q and fresh_fruit:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_fruit -= 1
                        q.append([nr, nc])
            elapsed_time += 1


        return elapsed_time if fresh_fruit == 0 else -1

