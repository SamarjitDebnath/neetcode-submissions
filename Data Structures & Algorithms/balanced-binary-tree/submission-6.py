# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def height_util(self, node: Optional[TreeNode]) -> int:
    #     if not node: return 0
        
    #     lh = self.height_util(node.left)
    #     rh = self.height_util(node.right)

    #     return max(lh, rh) + 1

    def checker(self, node: Optional[TreeNode]) -> int:
        if not node: return 0

        lh = self.checker(node.left)
        rh = self.checker(node.right)

        if abs(lh - rh) > 1 or lh == -1 or rh == -1:
            return -1

        return max(lh, rh) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if not root: return True

        # lh = self.height_util(root.left)
        # rh = self.height_util(root.right)

        # if abs(lh - rh) > 1:
        #     return False

        # left = self.isBalanced(root.left)
        # right = self.isBalanced(root.right)

        # if not left or not right:
        #     return False
        
        # return True

        if not root: return True

        return self.checker(root) > 0