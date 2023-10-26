from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        safe = [[False for _ in range(cols)] for _ in range(rows)]

        def bfs(queue):
            while queue:
                r, c = queue.popleft()

                for dr, dc  in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not safe[nr][nc] and board[nr][nc] == "O":
                        queue.append((nr, nc))
                        safe[nr][nc] = True

        for i in range(rows):
            if board[i][0] == "O" and not safe[i][0]:
                safe[i][0] = True
                bfs(deque([(i,0)]))
            if board[i][cols-1] == "O" and not safe[i][cols-1]:
                safe[i][cols-1] = True
                bfs(deque([(i,cols-1)]))
        

        for j in range(cols):
            if board[0][j] == "O" and not safe[0][j]:
                safe[0][j] = True
                bfs(deque([(0,j)]))
            if board[rows-1][j] == "O" and not safe[rows-1][j]:
                safe[rows-1][j] = True
                bfs(deque([(rows-1,j)]))
        
        
        for i in range(rows):
            for j in range(cols):
                if not safe[i][j] and board[i][j] == "O":
                    board[i][j] = "X"