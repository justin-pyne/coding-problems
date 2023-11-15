from typing import List
import heapq

class Solution:
    def euclidean(self, x: List[int]) -> int:
        return x[0]**2 + x[1]**2


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [(-self.euclidean(x), x) for x in points[:k]]
        heapq.heapify(max_heap)

        for point in points[k:]:
            dist = -self.euclidean(point)
            if dist > max_heap[0][0]:
                heapq.heappushpop(max_heap, (dist, point))

        return [point for _, point in max_heap]