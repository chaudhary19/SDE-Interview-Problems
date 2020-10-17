# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def heightUtility(self, root):
        
        if not root:
            return 0
        
        left = self.heightUtility(root.left)
        right = self.heightUtility(root.right)
        
        return max(left, right) + 1
    
    def maxDepth(self, root):
        
        ans = self.heightUtility(root)
        return ans
