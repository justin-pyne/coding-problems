from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        sort = []
        def listify(node: Optional[TreeNode], sort):
            if not node:
                return
            listify(node.left, sort)
            sort.append(node.val)
            listify(node.right, sort)

        listify(root, sort)
        return sort[k-1]
