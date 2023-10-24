from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
         
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            # base cases
            if r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or grid[r][c] == 0:
                return 0
            
            # update visited
            visited[r][c] = True

            # dfs
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area