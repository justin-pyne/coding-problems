from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([(root, 0)])
        result = []

        while queue:
            curr, level = queue.popleft()

            # check if new level
            if level == len(result):
                result.append([])
            
            result[level].append(curr.val)

            if curr.left:
                queue.append((curr.left, level+1))
            if curr.right:
                queue.append((curr.right, level+1))

        
        return result