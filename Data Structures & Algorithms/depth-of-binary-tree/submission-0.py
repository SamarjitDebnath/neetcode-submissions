# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def treeHeight(node: TreeNode) -> int:
            if not node:
                return 0
            leftHeight = treeHeight(node.left)
            rightHeight = treeHeight(node.right)
        
            return 1 + max(leftHeight, rightHeight)
        
        return treeHeight(root)