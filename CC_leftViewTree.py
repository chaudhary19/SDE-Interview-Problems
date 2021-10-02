'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def leftViewUtility(root, level, maxLevel, ans):
    
    if not root: return
    
    if level > maxLevel[0]:
        maxLevel[0] = level
        ans.append(root.data)
    
    leftViewUtility(root.left, level + 1, maxLevel, ans)
    leftViewUtility(root.right, level + 1, maxLevel, ans)

def LeftView(root):
    
    maxLevel = [0]
    ans = []
    leftViewUtility(root, 1, maxLevel, ans)
    return ans


# Time complexity: O(number of nodes)
# Space Complexity: O(1) auxiliary [O(height of tree) if we consider space used by stack]
