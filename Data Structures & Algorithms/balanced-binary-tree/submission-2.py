# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def _heightDiffUtil(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            lh = _heightDiffUtil(node.left)
            rh = _heightDiffUtil(node.right)

            if abs(lh - rh) > 1 or (lh == -1) or (rh == -1):
                return -1
            
            return 1 + max(lh, rh)

        return _heightDiffUtil(root) >= 0