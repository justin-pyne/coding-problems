class Solution:
    from typing import List
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        """
        num_set = set(nums)
        longest_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num+1 in num_set:
                    current_num += 1
                    current_length += 1
        
                longest_length = max(longest_length, current_length)
        
        return longest_length


