from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)

        while left <= right:

            k = (left+right)//2
            hours = sum((i+k-1)//k for i in piles)

            if hours <= h:
                right = k - 1
            else:
                left = k + 1
        
        return left