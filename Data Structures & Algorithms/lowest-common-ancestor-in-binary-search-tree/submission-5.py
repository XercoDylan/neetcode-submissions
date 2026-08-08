# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lowest = root
        current = root

        while (current != None):
            if current.left != None and p.val < current.val and q.val < current.val:
                current = current.left
                lowest = current
            elif current.right != None and p.val > current.val and q.val > current.val:
                current = current.right
                lowest = current
            else:
                current = None

        return lowest

        