from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        keep count of islands
        have visited 2d array, init all as false

        when we find unvisited land:
        update count
        dfs all land connected to this, mark all of the land as visited

        return count at the end
        """

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0

        def dfs(r, c):
            # base case
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0' or visited[r][c]:
                return

            # update visited
            visited[i][j] = True

            # dfs
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(i, j)
        
        return count