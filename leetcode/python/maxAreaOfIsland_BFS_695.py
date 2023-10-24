from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0]) 
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    count = 0
                    visited[i][j] = True
                    q = deque([(i, j)])

                    while q:
                        r, c = q.popleft()
                        count += 1

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                    
                    max_area = max(max_area, count)
        
        return max_area

                        