class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None
        ROW = len(board)
        COL = len(board[0])

        def dfs(i, j, board):
            if i < 0 or j < 0 or i >= ROW or j >= COL or board[i][j] == "X" or board[i][j] == "S":
                return

            board[i][j] = "S"
            dfs(i + 1, j, board)
            dfs(i, j + 1, board)
            dfs(i - 1, j, board)
            dfs(i, j - 1, board)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "O" and (i == 0 or i == ROW - 1 or j == 0 or j == COL - 1):
                    dfs(i, j, board)
        
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"

        