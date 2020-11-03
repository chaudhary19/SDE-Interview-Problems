# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        
        ptr = root
        while ptr:
            if ptr.val == val:
                return ptr
            elif ptr.val < val:
                ptr = ptr.right
            else:
                ptr = ptr.left
        return None
