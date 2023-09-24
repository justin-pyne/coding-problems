class Solution:
    from typing import List

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pass

        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return[left+1, right+1]