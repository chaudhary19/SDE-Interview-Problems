# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def Postorder(self, root):
        
        if root:
            self.Postorder(root.left)
            self.Postorder(root.right)
            self.ans.append(root.val)
    
    def postorderTraversal(self, root):
        
        self.ans = []
        self.Postorder(root)
        return self.ans
        
