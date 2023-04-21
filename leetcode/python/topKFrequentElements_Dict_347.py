class Solution:
    from typing import List

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        create a dict with elements and their count
        sort the list of elements by their count
        grab the first k elements when elements are ordered descending
        """

        from collections import Counter
        
        count = Counter(nums)
        unique_elements = list(count.keys())
        unique_elements.sort(key=lambda x: count[x], reverse = True)

        return unique_elements[:k]