def twoSumHM(nums, target):
    """
    nums = [2,7,11,15], target = 9
    return [0, 1]
    edge case:
    2*num = target
    want to avoid returning two of the same index
    ex:
    nums = [3, 3]
    do not want output = [0, 0] or loop to be stopped

    sol:
    check b4 adding to dict

    dict format:
    key: num
    value: index
    """
    d = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in d and i != d[complement]:
            return [d[complement], i]
        d[n] = i


# nums = [2,7,11,15]
# target = 9
# print(twoSumHM(nums, target))