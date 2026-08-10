# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Reverse PreOrder
        # Root -> Right -> Left
        def _reversePreOrder(node: Optional[TreeNode], res: List[int] = [], current_level = 0) -> List[int]:
            if not node:
                return

            if len(res) == current_level:
                res.append(node.val)
            
            _reversePreOrder(node=node.right, res=res, current_level=current_level+1)
            _reversePreOrder(node=node.left, res=res, current_level=current_level+1)

        if not root:
            return []

        res = []
        _reversePreOrder(node=root, res=res, current_level=0)

        return res