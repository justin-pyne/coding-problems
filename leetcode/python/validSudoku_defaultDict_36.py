class Solution:
    from typing import List 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #define sets
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        #loop through board
        for row in range(9):
            for col in range(9):
                #define vars
                num = board[row][col]
                grid_index = (row//3, col//3)

                #pass empty cells
                if num == ".":
                    continue

                #check conditions
                if (
                    num in rows[row]
                    or num in cols[col]
                    or num in grid[grid_index]
                ):
                    return False

                #add to sets
                rows[row].add(num)
                cols[col].add(num)
                grid[grid_index].add(num)

        return True
