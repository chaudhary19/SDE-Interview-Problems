'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def topViewUtility(root, height, width, mydict):
    
    if not root:
        return
    
    if (width not in mydict) or (mydict[width][1] > height):
        mydict[width] = (root.data, height)
    
    topViewUtility(root.left, height + 1, width - 1, mydict)
    topViewUtility(root.right, height + 1, width + 1, mydict)

def topView(root):
    
    mydict = dict()
    topViewUtility(root, 0, 0, mydict)       # root, height, width, map
    
    for key in sorted(mydict.keys()):
        print(mydict[key][0], end=' ')

# sort them only when someone ask to print from left to right or vice versa...
