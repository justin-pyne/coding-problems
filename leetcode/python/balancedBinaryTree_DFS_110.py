# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    from typing import Optional

    def depth(self, node: Optional[TreeNode]) -> int:
        """
        return -1 if not balanced
        return 0 for no root
        return depth
        """

        if not node:
            return 0
        leftMax = self.depth(node.left)
        rightMax = self.depth(node.right)
        
        if leftMax < 0 or rightMax < 0 or abs(leftMax - rightMax) > 1:
            return -1

        return 1 + max(leftMax, rightMax)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.depth(root) >= 0