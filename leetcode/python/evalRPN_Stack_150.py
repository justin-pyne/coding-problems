from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        use stack to track numbers, pop top 2 from stack when hit an operand, repush to stack

        cast return and popped numbers to ints, cast division to int to round
        """
        stack = []
        op = ['+', '-', '*', '/']

        for char in tokens:
            if char in op:
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(y+x if char == '+' else y-x if char == '-' else y*x if char == '*' else int(y/x))
            else:
                stack.append(char)
        
        return int(stack[-1])