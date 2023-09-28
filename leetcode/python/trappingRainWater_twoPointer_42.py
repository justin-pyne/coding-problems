class Solution:
    from typing import List

    def trap(self, height: List[int]) -> int:
        """
        twoPointer approach:

        at EACH index:
        find the max elements to both the right and the left (store these as leftMax, rightMax)
        use two pointers, left and right, to traverse the list from both ends

        water at each element:
        if height[left] <  height[right]:
            if height[left] > leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:

        work element by element, add water if applicable

        logic to change leftMax and rightMax:
        if height[left] > leftMax:



        examples:
        first example (both ways)
        left to right case:
        0, 1, 0, 2, 1, 0, 1, 3

        right to left case:
        3, 1, 0, 1, 2, 0, 1, 0

        4, 2, 0, 3, 2, 5
                  =
        =         =
        =     =   =
        = =   = = =
        = = _ = = =

        """

        if not height:
            return 0
        

        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right -= 1
                
        return water