from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                return True
            else:
                d[n] = i
        return False
