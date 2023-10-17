from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        backtracking solution:

        create backtrack function with following parameters:
        index: current index we are checking
        target: remaining # until we hit target
        current = []: our current list of sum

        @ each index, if # @ index is less than target, we can include it
        call backtrack with updated target @ same index
        pop from current and continue

        if not less than target/after pop, move index ands continue
        """

        res = []

        def backtrack(index, target, current = []):
            # base case
            if index == len(candidates):
                if target == 0:
                    res.append(current[:])
                return
            
            # include
            if candidates[index] <= target:
                current.append(candidates[index])
                backtrack(index, target-candidates[index])
                current.pop()
            
            # continue
            backtrack(index+1, target)

        backtrack(0, target)
        return res