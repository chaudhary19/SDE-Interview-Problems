# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def helpInorder(self, root):
        
        if root:
            self.helpInorder(root.left)
            self.ans.append(root.val)
            self.helpInorder(root.right)
    
    def inorderTraversal(self, root):
        
        self.ans = []
        self.helpInorder(root);
        return self.ans
            
        
