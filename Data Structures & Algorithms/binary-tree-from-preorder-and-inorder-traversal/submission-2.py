# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def _util(inord, ins, ine, preord, ps, pe, inmap) -> Optional[TreeNode]:
            if (ps > pe) or (ins > ine): return
            
            # build TreeNode
            root = TreeNode(preord[ps])

            # get the element from inorder to process
            in_root = inmap[root.val]
            numsleft = in_root - ins

            # recursively build left and right subtree
            root.left = _util(inord, ins, (in_root - 1), preord, (ps + 1), (ps + numsleft), inmap)
            root.right = _util(inord, (in_root + 1), ine, preord, (ps + numsleft + 1), pe, inmap)

            return root

        inmap = {}

        for i, elem in enumerate(inorder):
            inmap[elem] = i

        return _util(inorder, 0, len(inorder)-1, preorder, 0, len(preorder)-1, inmap)
