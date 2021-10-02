# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def diameterUtility(self, root):
        
        if not root:
            return 0
        
        left = self.diameterUtility(root.left)
        right = self.diameterUtility(root.right)
        
        self.ans = max(self.ans, left + right)
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root):
        
        self.ans = 0
        self.diameterUtility(root)
        return self.ans
