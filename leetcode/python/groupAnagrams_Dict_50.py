from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [""]
        
        anagrams = {}
        for word in strs:
            temp = ''.join(sorted(word))
            if temp in anagrams:
                anagrams[temp].append(word)
            else:
                anagrams[temp] = [word]
        return list(anagrams.values())
