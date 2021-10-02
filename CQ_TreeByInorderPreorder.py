# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def create_node(self, start, end):
        
        if start > end:
            return None
        
        node = TreeNode(self.preorder[self.pre_idx])
        self.pre_idx += 1
        
        in_idx = self.mydict[node.val]
        
        node.left = self.create_node(start, in_idx - 1)
        node.right = self.create_node(in_idx + 1, end)
        
        return node
    
    def buildTree(self, preorder, inorder):
        
        self.preorder = preorder
        self.inorder = inorder
        
        self.mydict = dict()
        for index, value in enumerate(inorder):
            self.mydict[value] = index
        
        self.pre_idx = 0
        
        return self.create_node(0, len(preorder) - 1)
