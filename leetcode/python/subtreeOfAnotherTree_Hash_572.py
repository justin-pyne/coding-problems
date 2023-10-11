# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    from typing import Optional

    def __init__(self):
        self.tree_hashes = set()
        self.b = 100000007
        self.p = 1000000009
    

    def tree_hash(self, node: Optional[TreeNode], target_hash: int, subRoot: Optional[TreeNode] ) -> int:
        """
        
        """
        if not node:
            return 0
        cur_hash = (self.tree_hash(node.left, target_hash, subRoot) + pow(self.b, node.val, self.p) + self.tree_hash(node.right, target_hash, subRoot))%self.p

        self.tree_hashes.add(cur_hash)

        if cur_hash == target_hash:
            if self.check(node, subRoot):
                 self.found = True
        return cur_hash

    
    def check(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return root.val == subRoot.val and self.check(root.left, subRoot.left) and self.check(root.right, subRoot.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sub_hash = self.tree_hash(subRoot, None, None)
        self.tree_hashes.clear()

        self.found = False
        self.tree_hash(root, sub_hash, subRoot)

        return self.found
