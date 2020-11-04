# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def solve(self, start, end, nums):
        
        if start > end:
            return None
        
        mid = start + (end - start + 1)//2
        node = TreeNode(nums[mid])
        
        node.left = self.solve(start, mid - 1, nums)
        node.right = self.solve(mid + 1, end, nums)
        
        return node
    
    def sortedArrayToBST(self, nums):
        
        length = len(nums)
        
        return self.solve(0, length - 1, nums)
        
