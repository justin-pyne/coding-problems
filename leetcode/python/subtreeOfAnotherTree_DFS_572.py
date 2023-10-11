# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    from typing import Optional

    def check(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        check function:
        check if two subtrees are the same:
        if not and not:
            return True
        if not or not:
            return False:
        return if vals same and left and right checks same
        """

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return root.val == subRoot.val and self.check(root.left, subRoot.left) and self.check(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val == subRoot.val:
            if self.check(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)