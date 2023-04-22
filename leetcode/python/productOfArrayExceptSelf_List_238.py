class Solution:
    from typing import List
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        construct ans through left product and right product
        """
        length = len(nums)
        answer = [1]*length

        #left product
        left = 1
        for i in range(length):
            answer *= left
            left *= nums[n]
        
        #right product
        right = 1
        for i in range(length-1, -1, -1):
            answer *= right
            right *= nums[i]
        
        return answer