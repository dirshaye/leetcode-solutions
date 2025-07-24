# LeetCode 145: Binary Tree Postorder Traversal
# Problem: https://leetcode.com/problems/binary-tree-postorder-traversal/
# Language: Python
# Approach: Recursive DFS (Postorder: Left -> Right -> Root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Base case: if the current node is None, return an empty list
        if not root:
            return []
        
        # Traverse left subtree, then right subtree, then visit the root node
        return (
            self.postorderTraversal(root.left) +
            self.postorderTraversal(root.right) +
            [root.val]
        )
