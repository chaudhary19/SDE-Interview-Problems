# lets try with Morris traversal.....

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorderTraversal(self, root):
        
        ans = []
        while root:
            
            if root.left:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    ans.append(root.val)
                    root = root.right
            else:
                ans.append(root.val)
                root = root.right
        return ans
        
