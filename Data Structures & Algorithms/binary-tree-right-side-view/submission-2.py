# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def _rev_preorder(node: Optional[TreeNode], res: list, curr_level: int):
            if not node: return

            if len(res) == curr_level:
                res.append(node.val)

            _rev_preorder(node.right, res, curr_level+1)
            _rev_preorder(node.left, res, curr_level+1)

        res = []
        _rev_preorder(root, res, curr_level=0)

        return res