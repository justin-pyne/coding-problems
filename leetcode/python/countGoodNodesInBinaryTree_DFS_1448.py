# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        dfs
        keep track of max val on each path
        update val and update count
        """

        def solve (node: TreeNode, val) -> int:
            if not node:
                return 0
            
            count = solve(node.left, max(val, node.val)) + solve(node.right, max(val, node.val))
            if node.val >= val:
                count += 1
            return count

        return solve(root, root.val)
            