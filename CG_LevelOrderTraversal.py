from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        
        ans = []
        if not root: return ans
        
        Q = deque()
        Q.append(root)
        curr = 1
        
        while Q:
            temp = []
            count = 0
            for i in range(curr):
                node = Q.popleft()
                temp.append(node.val)
                
                if node.left:
                    Q.append(node.left)
                    count += 1
                if node.right:
                    Q.append(node.right)
                    count += 1
            curr = count
            ans.append(temp)
        
        return ans
