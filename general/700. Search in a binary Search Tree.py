# LeetCode 700: Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Recursively searches for a node with the given value in a Binary Search Tree (BST)
        and returns the subtree rooted at that node. If not found, returns None.

        Time Complexity: O(h), where h is the height of the tree
        Space Complexity: O(h), due to recursion stack
        """
        if not root:
            return None

        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
