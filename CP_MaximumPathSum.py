# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def helper(self, root):
        
        if not root:
            return root
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        left = 0 if left is None else (left if left > 0 else 0)
        right = 0 if right is None else (right if right > 0 else 0)
        
        self.ans = max(self.ans, left + right + root.val)
        return max(left, right) + root.val
    
    def maxPathSum(self, root):
        
        self.ans = -float("inf")
        self.helper(root)
        return self.ans
