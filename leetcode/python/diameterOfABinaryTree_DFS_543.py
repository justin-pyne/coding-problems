# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    from typing import Optional
    """
    class variable: diameter

    depth function:
        1. calculate depth of left and right
        2. update diameter if larger @ this node
        3. return max DEPTH

        
    diameter function:
        1. call for depth at root
        2. return diameter
    """

    def __init__(self):
        self.diameter = 0

    def depth(self, node: Optional[TreeNode]) -> int:
        # calculate depth of left and right
        leftMax = self.depth(node.left) if node.left else 0
        rightMax = self.depth(node.right) if node.right else 0

        # calculate diameter @ this node
        if leftMax + rightMax > self.diameter:
            self.diameter = leftMax + rightMax

        # return max depth
        return 1 + max(leftMax, rightMax)



    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.diameter