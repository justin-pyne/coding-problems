class Solution:
    from typing import List

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        use counter to create dict with elements and count
        store tuples of (freq, element) in tuples in a minheap.
        we want the k most frequent elements
        - init heap with first k elements
        for all other elements in the dict
        - push new element into heap
        - when over k elements, pop root

        printing answer:
        extract the elements from the tuples
        _, num in min_heap
        """
        
        from collections import Counter
        import heapq

        count = Counter(nums)

        min_heap = [(freq, num) for num, freq in list(count.items())[:k]]
        heapq.heapify(min_heap)
    
        for num, freq in list(count.items())[k:]:
            heapq.heappushpop(min_heap, (freq, num))
        
        top_k = [num for _, num in min_heap]

        return top_k


