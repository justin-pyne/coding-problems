from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()


        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: # skipping duplicate values for firstNum
                continue
        
            firstNum = nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                secondNum = nums[j]
                thirdNum = nums[k]
                total = firstNum + secondNum + thirdNum

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    triplets.add((firstNum, secondNum, thirdNum))
                    j, k = j+1, k-1

                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1

        return triplets


