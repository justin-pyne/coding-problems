from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node: Optional[TreeNode], min_val = float('-inf'), max_val = float('inf')) -> bool:
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
    
        return validate(root)