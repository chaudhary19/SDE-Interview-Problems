# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorderTraversal(self, root):
        
        ans = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            ans.append(node.val)
            root = node.right
        
        return ans
            
        
