# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def _isSameTree(p, q):
            if not p or not q:
                return p == q

            return p.val == q.val and _isSameTree(p.left, q.left) and _isSameTree(p.right, q.right)


        # if _isSameTree(root, subRoot):
        #     return True
        
        return _isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
