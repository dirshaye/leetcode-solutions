# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Recursive Preorder Traversal of a Binary Tree.

        Args:
        root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        List[int]: A list containing the preorder traversal of the tree.
        """
        if not root:
            return []
        
        # Preorder: Root -> Left -> Right
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
