from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        BFS:
        """
        rows, cols = len(rooms, len(rooms[0]))
        q = deque()
        empty = 2147483647

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i, j))
        

        distance = 1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == empty:
                        rooms[nr][nc] = distance
                        q.append((nr, nc))
            distance += 1