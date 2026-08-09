# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], current = None) -> bool:

        if not current:
            current = [-float("inf"), float("inf")]
        

        if root.left:
            new_current = [current[0], min(current[1], root.val)]

   
    

            if root.left.val <= new_current[0]  or root.left.val >= new_current[1]:
                return False
            else:
                if not self.isValidBST(root.left, new_current):
                    return False

        if root.right:
            new_current = [max(current[0], root.val), current[1]]
 
            if root.right.val <= new_current[0]  or root.right.val >= new_current[1]:
                return False
            else:
                if not self.isValidBST(root.right, new_current):
                    return False


        return True
        