# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = True
        def solve(root):
            nonlocal bal
            if root is None:
                return 0
            leftheight = solve(root.left)
            rightheight = solve(root.right)
            if abs(leftheight - rightheight)!=1 and abs(leftheight - rightheight)!=0:
                bal = False
            return 1+max(leftheight,rightheight)
        solve(root)
        return bal
        
        