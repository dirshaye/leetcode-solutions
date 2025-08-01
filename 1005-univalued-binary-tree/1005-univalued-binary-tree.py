# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def check(node, value):
            if not node:
                return True

            if node.val != value:
                return False

            left = check(node.left, value)
            right = check(node.right, value)

            return left and right

        return check(root, root.val)
        