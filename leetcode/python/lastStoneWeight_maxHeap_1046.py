from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-val for val in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            newStone = abs(heapq.heappop(heap)) - abs(heapq.heappop(heap))
            if newStone != 0:
                heapq.heappush(heap, -1*newStone)
        
        return 0 if not heap else -1*heap[0]