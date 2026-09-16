class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])
        
        for r in range(ROW):
            for c in range(COL):
                # if curr is an 0
                if board[r][c] == "O":
                    # If O is on the border
                    if (r == 0 or c == 0
                        or r == ROW - 1 or c == COL - 1):
                        self.dfs(r, c, board)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

    def dfs(self, r, c, board):
        # If not out of range and already seen or it is not a "0"
        if (r < 0 or c < 0 or 
            r >= len(board) or c >= len(board[0]) or board[r][c] != "O"):
            return

        board[r][c] = "T" # flip to a temporary value
        
        self.dfs(r+1, c, board)
        self.dfs(r, c+1, board)
        self.dfs(r-1, c, board)
        self.dfs(r, c-1, board)

