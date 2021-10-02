"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        
        stack = []
        prev = None
        
        while root or stack:
            # print(root.val)
            
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            if prev and prev.val == p.val:
                
                return node
            
            root = node.right
            prev = node
        
        return None

# easy to find predecessor as well, just use previous and current pointer in opposite way :)
