class Solution:
    from typing import List
    #Note: this solution is suboptimal and does not meet the requirement of O(n) time, it is done for practice.
    def longestConsecutive(self, nums: List[int]) -> int:
        pass
        #vars
        count = 1
        longest = 1

        nums.sort()
        
        #edge case, empty list
        if not nums:
            return 0

        for i in range(1, len(nums)):
            #consecutive
            if nums[i] == nums[i-1] + 1:
                count += 1

            #duplicate
            elif nums[i] == nums[i-1]:
                continue

            #neither
            else:
                longest = max(longest, count)
                count = 1
    
        return max(longest, count)