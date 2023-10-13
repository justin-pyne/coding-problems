from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx = 0, current = []):
            # base case
            if idx == len(nums):
                res.append(current[:])
                return

            # include num @ idx
            current.append(nums[idx])
            backtrack(idx+1, current)

            # exclude num @ idx
            current.pop()
            backtrack(idx+1, current)

        backtrack()
        return res