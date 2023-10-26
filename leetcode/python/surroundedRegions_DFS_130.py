from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        variables:
        safe = 2d boolean visited array
        

        Note: any mass that isnt surrounded must be connected to a border O.
        So, dfs from border O, mark any visited land as safe.
        After dfsing all border nodes, loop through the array and convert every O that isnt safe.
        """

        rows, cols = len(board), len(board[0])
        safe = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            # base case
            if r < 0 or c < 0 or r >= rows or c >= cols or safe[r][c] or board[r][c] == "X":
                return
            
            # update visited
            safe[r][c] = True

            # dfs
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r+dr, c+dc)
        
        # loop through border nodes
        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][cols-1] == "O":
                dfs(i, cols-1)

        for j in range(cols):
            if board[0][j] == "O":
                dfs(0, j)
            if board[rows-1][j] == "O":
                dfs(rows-1, j)
        
        # loop through and modify board
        for i in range(rows):
            for j in range(cols):
                if not safe[i][j] and board[i][j] == "O":
                    board[i][j] = "X"
        