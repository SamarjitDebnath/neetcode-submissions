# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        
        if not subRoot: return True

        def _sameTreeUtil(p, q):
            if not p or not q:
                return (p == q)

            return (p.val == q.val) and _sameTreeUtil(p.left, q.left) and _sameTreeUtil(p.right, q.right)

        if _sameTreeUtil(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)