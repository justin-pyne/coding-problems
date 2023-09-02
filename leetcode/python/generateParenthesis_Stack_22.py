from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        solution = []

        def backtrack(openNum, closedNum):

            #base case
            if openNum == closedNum == n:
                solution.append("".join(stack))
                return
            
            if openNum < n:
                stack.append('(')
                backtrack(openNum+1, closedNum)
                stack.pop()
            
            if closedNum < openNum:
                stack.append(')')
                backtrack(openNum, closedNum+1)
                stack.pop()
            
        
        backtrack(0,0)
        return solution