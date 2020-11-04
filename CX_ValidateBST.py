# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def checkValidBST(self, minimum, maximum, node):
        
        if not node:
            return True
        
        if node.val < minimum or node.val > maximum:
            return False
        return self.checkValidBST(minimum, node.val - 1, node.left) and self.checkValidBST(node.val + 1, maximum, node.right)
    
    def isValidBST(self, root):
        
        return self.checkValidBST(-float('inf'), float('inf'), root)
