from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        
        ans = []
        if not root: return ans
        
        Q = deque()
        Q.append(root)
        
        count = 1
        flag = 1
        
        while Q:
            
            curr = 0
            temp = []
            
            for i in range(count):
                node = Q.popleft()
                temp.append(node.val)
                
                if node.left:
                    Q.append(node.left)
                    curr += 1
                
                if node.right:
                    Q.append(node.right)
                    curr += 1
                
            ans.append(temp[::flag])
            count  = curr
            flag *= -1
        
        return ans
