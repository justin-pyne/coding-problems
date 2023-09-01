class Solution:
    def isValid(self, s: str) -> bool:
        """
        secondary solution for validparenthesis, using continue instead to avoid double nesting.

        use stack to track open brackets

        for each closed bracket:
            if stack empty return false
            pop top element of stack, check that it is the same as the bracket
            else return false
        return true at end of looping through string 
        """
        openList = []

        for bracket in s:
            if bracket == '[' or bracket == '{' or bracket == '(':
                openList.append(bracket)
                continue
            
            if len(openList) == 0:
                    return False
                
            open = openList.pop()
            if bracket == ']' and open != '[' or bracket == '}' and open != '{' or bracket == ')' and open != '(':
                return False
        
        if len(openList) != 0:
            return False
        
        return True