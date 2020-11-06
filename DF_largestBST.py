# find the size of largest BST in Binary Tree

class TreeNode(object):
    
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class SubTreeInfo(object):
    
    def __init__(self, minimum, maximum, size, isBST):
        
        self.minimum = minimum
        self.maximum = maximum
        self.size = size
        self.isBST = isBST

def largestBST(root):
    
    if not root:
        return SubTreeInfo(float('inf'), -float('inf'), 0, True)
    
    left = largestBST(root.left)
    right = largestBST(root.right)
    
    if left.isBST and right.isBST and (left.maximum < root.data < right.minimum):
        
        info = SubTreeInfo(min(root.data, min(left.minimum, right.minimum)), max(root.data, max(left.maximum, right.maximum)), left.size + 1 + right.size, True)
    
    else:
        info = SubTreeInfo(0, 0, max(left.size, right.size), False)
    
    return info

if __name__ == '__main__':
    
    root = TreeNode(10)
    
    root.left = TreeNode(15)
    root.right = TreeNode(8)
    
    root.left.left = TreeNode(12)
    root.left.right = TreeNode(20)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(9)
    
    root.left.left.left = TreeNode(2)
    root.left.left.right = TreeNode(14)
    root.right.left.left = TreeNode(4)
    root.right.left.right = TreeNode(7)
    root.right.right.right = TreeNode(10)
    
    print("The size of largest BST is ", largestBST(root).size)
    
    
