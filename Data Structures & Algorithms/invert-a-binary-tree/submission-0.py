# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recursiveSolution(root)
        return root

    def recursiveSolution(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        head = root
        left = root.left
        right = root.right
        self.recursiveSolution(left)
        self.recursiveSolution(right)

        head.right = left
        head.left = right


               
