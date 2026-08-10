# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def _diameterUtil(node: Optional[TreeNode], diameter: list[int] = []):
            # return None if root is null
            if not node:
                return 0

            # run for left and right subtree
            lh = _diameterUtil(node.left, diameter)
            rh = _diameterUtil(node.right, diameter)

            # check for max path 
            diameter[0] = max(diameter[0], (lh+rh))

            # takes care of both left and right height that's how
            # we don't need two times to find the height -> optimisation to O(n)
            return 1 + max(lh, rh)

        diameter = [0]
        _diameterUtil(root, diameter)
        return diameter[0]