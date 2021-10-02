# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def preorderTraversal(self, root):
        
        stack = []
        ans = []
        
        while root or stack:
            while root:
                stack.append(root)
                ans.append(root.val)
                root = root.left
            root = stack.pop().right
        
        return ans
        
