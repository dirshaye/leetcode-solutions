# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        index = [0]
        def build(bound = float('inf')):
            if index[0] == len(preorder) or preorder[index[0]] > bound:
                return None

            value = preorder[index[0]]
            index[0] +=1

            root = TreeNode(value)
            root.left = build(root.val)
            root.right = build(bound)

            return root

        return build()



        