# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def rightSideUtility(self, root, currLevel):
        
        if not root:
            return 
        
        if currLevel > self.maxLevel:
            self.maxLevel = currLevel
            self.ans.append(root.val)
        
        self.rightSideUtility(root.right, currLevel + 1)
        self.rightSideUtility(root.left, currLevel + 1)
        
    
    def rightSideView(self, root):
        
        self.ans = []
        self.maxLevel = 0
        self.rightSideUtility(root, 1)
        return self.ans
                    
        
        
