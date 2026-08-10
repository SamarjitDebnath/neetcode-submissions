# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Time: O(n^2), Space: O(h)
        # def nodeHeight(node: TreeNode) -> int:
        #     if not node:
        #         return 0
        #     leftHeight = nodeHeight(node.left)
        #     rightHeight = nodeHeight(node.right)

        #     return 1 + max(leftHeight, rightHeight)

        # # calculate the length along left, right
        # leftNodeHeight = nodeHeight(root.left)
        # rightNodeHeight = nodeHeight(root.right)
        # height_through_root = leftNodeHeight + rightNodeHeight

        # # recursively find for all the left and right subtrees
        # leftDiameter = self.diameterOfBinaryTree(root.left)
        # rightDiameter = self.diameterOfBinaryTree(root.right)

        # return max(leftDiameter, rightDiameter, height_through_root)

        maxDiameter = 0
        def binrayTreeDiameterUtil(node: TreeNode) -> int:
            nonlocal maxDiameter
            if not node:
                return 0

            leftHeight = binrayTreeDiameterUtil(node.left)
            rightHeight = binrayTreeDiameterUtil(node.right)

            maxDiameter = max(maxDiameter, (leftHeight + rightHeight))
            
            return 1 + max(leftHeight, rightHeight)
        
        binrayTreeDiameterUtil(root)
        
        return maxDiameter
