from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def helper(preorder_start, inorder_start, inorder_end):
            if preorder_start >= len(preorder) or inorder_start > inorder_end:
                return None

            root_val = preorder[preorder_start]
            root = TreeNode(root_val)

            root_idx = inorder_map[root_val]

            root.left = helper(preorder_start + 1, inorder_start, root_idx-1)
            root.right = helper(preorder_start + (root_idx - inorder_start) + 1, root_idx + 1, inorder_end)

            return root
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, 0, len(inorder))