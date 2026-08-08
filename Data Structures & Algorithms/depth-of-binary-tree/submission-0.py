# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        depth1 = self.maxDepth(root.left) + 1
        depth2 = self.maxDepth(root.right) + 1

        return max(depth1, depth2)


        