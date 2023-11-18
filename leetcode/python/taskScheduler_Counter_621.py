from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counterDict = Counter(tasks)
        numTasks = len(tasks)
        maxVal = max(counterDict.values())
        totalMax = sum(1 for i in counterDict if counterDict[i] == maxVal)

        case1 = (maxVal-1) * (n+1) + totalMax

        return max(case1, numTasks)