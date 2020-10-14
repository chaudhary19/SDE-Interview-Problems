# lets do this using stack...

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def postorderTraversal(self, root):
        
        stack = []
        ans = []
        
        while stack or root:
            while root:
                stack.append(root)
                ans.append(root.val)
                root = root.right
            root = stack.pop().left
        
        return ans[::-1]
        
