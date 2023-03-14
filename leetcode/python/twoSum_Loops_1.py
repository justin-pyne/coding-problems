def twoSumLoops(nums, target):
    """
    nums = [2,7,11,15], target = 9
    return [0, 1]
        
    """
    for i, n in enumerate(nums):
        for j, k in enumerate(nums):
            if i != j and n + k == target:
                return [i, j]
                
# Test Case
# nums = [2,7,11,15]
# target = 9
# print(twoSumLoops(nums, target))