class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        for loop
            update the count
            update the maxChar length

            check if we have passed k, if so:
                remove count from 1 of that charcater
                increase left by 1 (move sliding window)
            
            r - left - maxChar + 1 = # of available other chars
        return r - left + 1
        
        
        ABAB k = 2

        """

        count = {}
        left = 0
        maxChar = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxChar = max(maxChar, count[s[r]])

            if r - left - maxChar + 1 > k:
                count[s[left]] -= 1
                left += 1
        
        return r - left + 1


            