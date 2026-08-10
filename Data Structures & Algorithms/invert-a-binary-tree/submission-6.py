# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS recursion: Either Pre or Post Order
        # if not root:
        #     return None

        
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # root.left, root.right = root.right, root.left

        # return root

        # BFS: Stack

        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()

            # swap the variables
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        return root
