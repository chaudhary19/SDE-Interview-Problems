# a perfect postorder using stack and not reversing preOrder

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def postorderTraversal(self, root):
        
        ans = []
        if not root: return ans
        
        stack = [root] * 2
        
        while stack:
            curr = stack.pop()
            if stack and stack[-1] == curr:
                if curr.right:
                    stack += [curr.right] * 2
                if curr.left:
                    stack += [curr.left] * 2
            else:
                ans.append(curr.val)
        
        return ans
