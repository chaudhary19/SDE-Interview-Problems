from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def verticalTraversalUtility(self, root, height, width):
        
        if not root:
            return
        
        self.mydict[width].append((height, root.val))
        
        self.verticalTraversalUtility(root.left, height + 1, width - 1)
        self.verticalTraversalUtility(root.right, height + 1, width + 1)
    
    def verticalTraversal(self, root):
        
        self.mydict = defaultdict(list)
        self.verticalTraversalUtility(root, 0, 0)
        
        ans = []
        for key in sorted(self.mydict.keys()):
            temp = []
            for h, v in sorted(self.mydict[key]):
                temp.append(v)
            ans.append(temp)
    
        return ans
                                      
                                     
        
