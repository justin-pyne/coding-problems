from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        determime if left or right half is sorted
        determine if target is in sorted half
        if not then it is in the non-sorted half
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # left half is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else: # right half is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        
        return -1
