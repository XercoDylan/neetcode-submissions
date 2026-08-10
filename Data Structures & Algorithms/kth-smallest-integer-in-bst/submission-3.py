# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = []
        def helper(current_root):

            if current_root.left:
                helper(current_root.left)
            
            
            current.append(current_root.val)

            if len(current) == k:
                return current[-1]

            if current_root.right:
               helper(current_root.right)

        helper(root)

        return current[k - 1]