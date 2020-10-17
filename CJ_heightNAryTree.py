"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    
    def heightUtility(self, root):
        
        if not root:
            return 0
        
        ans = 0
        for child in root.children:
            ans = max(ans, self.heightUtility(child))
        return ans + 1 
    
    def maxDepth(self, root):
        
        ans = self.heightUtility(root)
        return ans
