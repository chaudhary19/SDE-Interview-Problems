# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def kthSmallest(self, root, k):
        
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            root = node.right
        
 
