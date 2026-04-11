# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Every recursive function needs to explicitly return a value in all paths
        def inorderTraversal(node,prev):
            # PATH 1: Empty node
            if not node:
                return True

            # PATH 2: check left subtree. Left subtree fails 
            if not inorderTraversal(node.left,prev):
                return False

            # PATH 3: Current node violates BST
            if node.val <= prev[0]:
                return False

            # Update prev
            prev[0] = node.val

            # PATH 4: Right subtree fails
            if not inorderTraversal(node.right,prev):
                return False

            # PATH 5: ALL checks passed!
            return True
        
        #Python's parameter passing, Mutable types (list, dict, set) 
        # → changes are propagated back
        prev = [float('-inf')]
        valid = inorderTraversal(root,prev)
        return valid
