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
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
        

        # bfs from border cells
        for i in range(rows):
            pacific[i][0] = True
            atlantic[i][cols-1] = True
            bfs(deque([(i, 0)]), pacific)
            bfs(deque([(i, cols-1)]), atlantic)
        
        for j in range(cols):
            pacific[0][j] = True
            atlantic[rows-1][j] = True
            bfs(deque([(0, j)]), pacific)
            bfs(deque([(rows-1, j)]), atlantic)
        
        res = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    res.append((i, j))
        return res


        return res
                    
