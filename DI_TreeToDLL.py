# convert Binary Tree into Doubly Linked List

class TreeNode(object):
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
class DLLNode(object):
    
    def __init__(self, data, prev=None, nxt=None):
        self.data = data
        self.prev = prev
        self.nxt = nxt

class TreeToDLL(object):
    
    def __init__(self, root):
        
        self.root = root                       # binary tree
        self.head = self.tail = None           # head and tail of doubly linked list
        
    def InOrder(self):
        
        self.inorderUtility(self.root)
    
    def inorderUtility(self, node):
        
        if node:
            self.inorderUtility(node.left)
            self.addToDLL(node.data)
            self.inorderUtility(node.right)
        else:
            return
    
    def addToDLL(self, val):
        
        new_node = DLLNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.nxt = new_node
            new_node.prev = self.tail
            self.tail = self.tail.nxt

    def printDLL(self):
        
        ptr = self.head
        while ptr:
            print(ptr.data, end=" ")
            ptr = ptr.nxt
            
    
if __name__ == "__main__":
    
    root = TreeNode(1)
    
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    obj = TreeToDLL(root)
    obj.InOrder()
    obj.printDLL()
