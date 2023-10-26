from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        dfs from every border cell (reaching border = reaching ocean)
        pacific, atlantic = False 2d array to track if water can flow
        rows, cols =


        def dfs(r, c, visited, prevHeight)


        dfs from every border cell

        check if True in both ocean arrays, if so append to result

        """

        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = [[False for _ in range(cols)] for _ in range(rows)], [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c, visited, prevHeight):
            # base case
            if r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or heights[r][c] < prevHeight:
                return
            
            # update visited
            visited[r][c] = True

            # dfs
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r+dr, c+dc, visited, heights[r][c])
            
        # dfs all border cells
        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols-1, atlantic, heights[i][cols-1])

        for j in range(cols):
            dfs(0, j, pacific, heights[0][j])
            dfs(rows-1, j, atlantic, heights[rows-1][j])
        

        # check if a cell can reach the atlantic and pacific
        res = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])

        return res
                    
