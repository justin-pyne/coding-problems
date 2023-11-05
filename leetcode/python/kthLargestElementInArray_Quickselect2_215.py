from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        
        while True:
            pivot_index = random.randint(left, right)
            new_pivot_index = self.partition(nums, left, right, pivot_index)
            if new_pivot_index == len(nums) - k:
                return nums[new_pivot_index]
            elif new_pivot_index > len(nums) - k:
                right = new_pivot_index - 1
            else:
                left = new_pivot_index + 1
            
    

    def partition(self, nums, left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        stored_index = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[stored_index], nums[i] = nums[i], nums[stored_index]
                stored_index += 1
        
        nums[stored_index], nums[right] = nums[right], nums[stored_index]
        return stored_index