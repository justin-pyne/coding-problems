class Solution:
    def isValid(self, s: str) -> bool:
        """
        use stack to track open parenthesis

        for each closed parenthesis:
            if len(openList) == 0 then return false

            else:
                if closed and open parenthesis dont match
                    return False
        
        if len(openList) is not 0
            return False
        
        return True
        """

        openList = []

        for bracket in s:
            if bracket == '[' or bracket == '{' or bracket == '(':
                openList.append(bracket)
            
            else:
                if len(openList) == 0:
                    return False
                
                open = openList.pop()
                if bracket == ']' and open != '[' or bracket == '}' and open != '{' or bracket == ')' and open != '(':
                    return False
        
        if len(openList) != 0:
            return False
        
        return True