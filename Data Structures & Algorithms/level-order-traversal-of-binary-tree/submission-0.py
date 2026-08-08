# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        transversal = []
        current_frontier = [root]

        while (len(current_frontier) > 0):
            transversal.append([tree.val for tree in current_frontier])
            next_frontier = []

            for tree in current_frontier:
                if tree.left:
                    next_frontier.append(tree.left)

                if tree.right:
                    next_frontier.append(tree.right)


            current_frontier = next_frontier




        return transversal
        