class TreeNode(object):
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findFloor(node, value):
    
    if not node:
        return -1
    
    if node.data == value:
        return node.data
    
    if node.data > value:
        return findFloor(node.left, value)

    val = findFloor(node.right, value)
    return node.data if node.data > val else val


root = TreeNode(8)

root.left = TreeNode(4)
root.left.left = TreeNode(2)        
root.left.right = TreeNode(6)

root.right = TreeNode(12)
root.right.right = TreeNode(14)
root.right.left = TreeNode(10)

for i in range(16):
    print("floor value of ", i, " = ", findFloor(root, i))
    
# floor value of  0  =  -1
# floor value of  1  =  -1
# floor value of  2  =  2
# floor value of  3  =  2
# floor value of  4  =  4
# floor value of  5  =  4
# floor value of  6  =  6
# floor value of  7  =  6
# floor value of  8  =  8
# floor value of  9  =  8
# floor value of  10  =  10
# floor value of  11  =  10
# floor value of  12  =  12
# floor value of  13  =  12
# floor value of  14  =  14
# floor value of  15  =  14
