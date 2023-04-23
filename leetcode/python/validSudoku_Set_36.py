class Solution:
    from typing import List    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #define sets
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]


        for row in range(9):
            for col in range(9):
                num = board[row][col]

                grid_index = (row//3)*3 + col//3

                #continue if empty cell
                if num == ".":
                    continue

                #check if in row, col, or grid
                if num in rows[row] or num in cols[col] or num in grid[grid_index]:
                    return False
                
                rows[row].add(num)
                cols[col].add(num)
                grid[grid_index].add(num)

        
        return True
