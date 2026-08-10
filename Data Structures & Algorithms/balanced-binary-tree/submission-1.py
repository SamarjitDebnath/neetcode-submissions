# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        balanced = False
        def heightUtil(node: TreeNode) -> int:
            nonlocal balanced
            if not node:
                return 0
            
            leftHeight, rightHeight = heightUtil(node.left), heightUtil(node.right)
            
            # If any subtree is unbalanced, propagate the result immediately.
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            
            return 1 + max(leftHeight, rightHeight)

        
        return heightUtil(root) != -1