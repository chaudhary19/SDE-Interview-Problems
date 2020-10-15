'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def bottomViewUtility(root, height, width, mydict):
    
    if not root:
        return
    
    if (width not in mydict) or (mydict[width][0] <= height):
        mydict[width] = (height, root.data)
    bottomViewUtility(root.left, height + 1, width - 1, mydict)
    bottomViewUtility(root.right, height + 1, width + 1, mydict)

def bottomView(root):
    
    mydict = dict()
    bottomViewUtility(root, 0, 0, mydict)
    ans = []
    
    for key in sorted(mydict.keys()):
        ans.append(mydict[key][1])
    return ans


