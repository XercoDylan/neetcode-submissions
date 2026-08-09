# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root):
            if root == None:
                return []

            stack = helper(root.left) + [root.val] + helper(root.right) 
            
            return stack

        stack = helper(root)

        return stack[k - 1]
            
                
        
        
        


        
        


        