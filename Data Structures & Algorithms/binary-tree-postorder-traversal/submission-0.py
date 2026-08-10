# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def _util(node, res):
            if not node: return

            _util(node.left, res)
            _util(node.right, res)
            res.append(node.val)

        res = []
        _util(root, res)
        return res