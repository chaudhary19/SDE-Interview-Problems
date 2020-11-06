# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        
        def doit(node):
            
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        
        
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        
        def doit():
            
            item = next(vals)
            if item == '#':
                return None
            else:
                node = TreeNode(int(item))
                node.left = doit()
                node.right = doit()
                return node
        
        vals = iter(data.split())
        return doit()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
