# Using Recursion-------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        
        if not root:
            return True
        return self.Symmetric(root.left, root.right)
    
    def Symmetric(self, l, r):
        
        if not l and not r:
            return True
        if not l or not r:
            return False
        
        if l.val == r.val:
            inPair = self.Symmetric(l.right, r.left)
            outPair = self.Symmetric(l.left, r.right)
            if inPair and outPair:
                return True
        return False
        
# -------------------------Stack based------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        while stack:
            
            left,right = stack.pop()
            
            if not left and not right:
                continue
            
            if not left or not right:
                return False
            
            if left.val == right.val:
                inside = (left.right, right.left)
                outside = (left.left, right.right)
                stack.append(inside)
                stack.append(outside)
            else:
                return False
        
        return True
