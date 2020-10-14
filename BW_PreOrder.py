# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def Preorder(self, root):
        
        if root:
            self.ans.append(root.val)
            self.Preorder(root.left)
            self.Preorder(root.right)
    
    def preorderTraversal(self, root):
        
        self.ans = []
        self.Preorder(root)
        return self.ans
        
