class TreeNode(object):
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findCeil(node, value):
    
    if not node:
        return -1

    if node.data == value:
        return node.data
    
    if node.data < value:
        return findCeil(node.right, value)
    
    val = findCeil(node.left, value)
    return val if val >= value else node.data

root = TreeNode(8)

root.left = TreeNode(4)
root.left.left = TreeNode(2)        
root.left.right = TreeNode(6)

root.right = TreeNode(12)
root.right.right = TreeNode(14)
root.right.left = TreeNode(10)

for i in range(1, 16):
    print("ceil value of ", i, " = ", findCeil(root, i))

# ceil value of  1  =  2  
# ceil value of  2  =  2  
# ceil value of  3  =  4  
# ceil value of  4  =  4  
# ceil value of  5  =  6  
# ceil value of  6  =  6  
# ceil value of  7  =  8  
# ceil value of  8  =  8  
# ceil value of  9  =  10 
# ceil value of  10  =  10
# ceil value of  11  =  12
# ceil value of  12  =  12
# ceil value of  13  =  14
# ceil value of  14  =  14
# ceil value of  15  =  -1
