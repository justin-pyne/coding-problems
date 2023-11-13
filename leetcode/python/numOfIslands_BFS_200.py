from typing import List
from collections import deque

deque.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    # found a new island
                    count += 1
                    visited[i][j] = True

                    q = deque([(i, j)])
                    while q:
                        r, c = q.popleft()

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == '1':
                                visited[nr][nc] = True
                                q.append((nr, nc))
        
        return count