from typing import List
import heapq

class Solution:

    def manhattan(self, p: List[int], q: List[int]):
        return abs(p[0] - q[0]) + abs(p[1] - q[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = [(0,0)]
        heap_dict = {0:0}
        visited = [False] * n
        totalCost = 0

        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if visited[node] or heap_dict.get(node, float('inf')) < weight:
                continue
            
            visited[node] = True
            totalCost += weight

            for newNode in range(n):
                if not visited[newNode]:
                    distance = self.manhattan(points[node], points[newNode])
                    if distance < heap_dict.get(newNode, float('inf')):
                        heap_dict[newNode] = distance
                        heapq.heappush(min_heap, (distance, newNode))

        return totalCost