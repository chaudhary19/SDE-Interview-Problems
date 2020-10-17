# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def UtilityCheck(self, root):
        
        if not root:
            return 0
        
        left = self.UtilityCheck(root.left)
        right = self.UtilityCheck(root.right)
        
        if abs(left - right) > 1: self.ans = False
        
        return max(left, right) + 1
    
    def isBalanced(self, root):
        
        self.ans = True
        self.UtilityCheck(root)
        return self.ans
        
