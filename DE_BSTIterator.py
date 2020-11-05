# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):

    def __init__(self, root):
        
        self.curr_node = root
        self.stack = []
        

    def next(self):
        
        while self.curr_node:
            self.stack.append(self.curr_node)
            self.curr_node = self.curr_node.left
        
        node = self.stack.pop()
        self.curr_node = node.right
        return node.val
        
    def hasNext(self):
    
        if self.curr_node or len(self.stack) > 0:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
