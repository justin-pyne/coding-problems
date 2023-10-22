from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]
        
        for _ in nums:
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)
            
            res.extend(perms)
            nums.append(n)
        
        return res