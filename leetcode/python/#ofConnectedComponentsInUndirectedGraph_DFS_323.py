from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(n):
            visited[n] = True
            for neighbor in graph[n]:
                if not visited[neighbor]:
                    dfs(neighbor)

        
        visited = [False for _ in range(n)]
        
        # adj list init
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        return count
        