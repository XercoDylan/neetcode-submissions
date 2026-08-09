# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(tree, minimum, maximum):
            if not tree:
                return True

            if not (minimum < tree.val < maximum):
                return False

            return isValid(tree.left, minimum, tree.val) and isValid(tree.right, tree.val, maximum)

        return isValid(root, float("-inf"), float("inf"))
        