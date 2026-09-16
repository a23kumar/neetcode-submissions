class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # the entrypoint of this can be simply iterating through all values in 2-d array
        ROW = len(board)
        COL = len(board[0])
        path = set()
        def dfs(ind, i, j):
            if ind == len(word):
                return True
            if i < 0 or j < 0 or i >= ROW or j >= COL or word[ind] != board[i][j] or (i, j) in path:
                return False
            
            path.add((i, j))
            res = (dfs(ind + 1, i+1, j) or 
                dfs(ind + 1, i, j+1) or 
                dfs(ind + 1, i-1, j) or 
                dfs(ind + 1, i, j-1))
            path.remove((i, j))
            return res

        for i in range(ROW):
            for j in range(COL):
                if dfs(0, i, j): return True
        return False
