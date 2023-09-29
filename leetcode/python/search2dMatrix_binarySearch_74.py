from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        binary search:
        convert index of 2d array to a 1d array:
            matrix[row][col]
            
            rowTotal = # of rows: len(matrix)
            colTotal = # of cols: len(matrix[0])

            row = index // colTotal
            col = index % colTotal

            colTotal*row + col
        
        def searchMatrix:
            rowTotal, colTotal = len(matrix), len(matrix[0])
            left, right = 0, (rowTotal*colTotal) - 1
        """

        rowTotal, colTotal = len(matrix), len(matrix[0])
        left, right = 0, (rowTotal*colTotal) - 1

        while left <= right:
            mid = (left + right) // 2
            midRow = mid // colTotal
            midCol = mid % colTotal

            current = matrix[midRow][midCol]

            if current == target:
                return True
            elif current > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False