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
        
        node = TreeNode(self.postorder[self.post_idx])
        self.post_idx -= 1
        
        in_idx = self.mydict[node.val]
        
        node.right = self.create_node(in_idx + 1, end)   # phle right call kro
        node.left = self.create_node(start, in_idx - 1)
        
        return node
        
    
    def buildTree(self, inorder, postorder):
        
        self.inorder = inorder
        self.postorder = postorder
        
        self.mydict = dict()
        
        for index, value in enumerate(inorder):
            self.mydict[value] = index
            
        self.post_idx = len(postorder) - 1        # root last me hoti hai na
        
        return self.create_node(0, len(postorder) - 1)
