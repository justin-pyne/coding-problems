from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        q = deque()
        
        # init q and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0

        # bfs traversal
        minute = -1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            size = len(q)
            for _ in range(size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        q.append((nr, nc))
            minute += 1
        
        return minute if fresh_oranges == 0 else -1

                    
