class Solution:
    def isPalindrome(self, s: str) -> bool:
        pass

        """
        method:
        use two pointers, left and right, to traverse the string from both ends

        while left < right: (while left and right haven't crossed each other meaning we are still traversing the string)
            while left is not alnum -> traverse left
            while right is not alnum -> traverse right

            if s[left] != s[right]:
                return false (not a palindrome, different values)

            else:
                left += 1
                right -= 1

                
        return True if all of this passes
        """

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and s[left].isalnum() == False:
                left += 1
            while left < right and s[right].isalnum() == False:
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            else:
                left += 1
                right -= 1
        
        return True