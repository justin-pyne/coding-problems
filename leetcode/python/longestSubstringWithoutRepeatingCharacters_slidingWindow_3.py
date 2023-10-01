class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window

        loop through the string
        charSet = current set of characters
        left = beginning index of the current substring
        res = length of longest substring

        abcabac
        """

        charSet = set()
        left = 0
        res = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[i])
            res = max(res, i - left +  1)
        return res