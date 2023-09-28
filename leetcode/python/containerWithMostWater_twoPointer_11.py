from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        left and right pointers
        store current maxArea, store difference between left and right for area calculation (and differences between leftSize and rightSize)
        at end of each iteration, compare currentArea to maxArea, if larger replace, else continue
        while left < right:
            if leftSize > rightSize:
                right -= 1
            elif right > left:
                left += 1


        # VARIABLES
        left = 0
        right = len(height) - 1
        maxArea = 0

        while:
            h = min(height[left], height[right])
            w = right - left
            currentArea = h * w

        """


        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(currentArea, maxArea)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea
        