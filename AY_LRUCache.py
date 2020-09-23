class Node(object):
    
    def __init__(self, key, value):
        
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    

class LRUCache(object):

    def __init__(self, capacity):
        
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.capacity = capacity
        self.length = 0
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.mydict = dict()
        

    def get(self, key):
        
        if key in self.mydict:
            node = self.mydict[key]
            self.delete(node)
            self.insert(node)
            return node.value
        
        return -1
        
    def put(self, key, value):
        
        if key in self.mydict:
            node = self.mydict[key]
            self.delete(node)
        
        new_node = Node(key, value)
        
        while self.length >= self.capacity:
            self.delete(self.head.next)
        
        self.insert(new_node)
    
    def delete(self, node):
        
        left = node.prev
        right = node.next
        
        left.next = right
        right.prev = left
        
        del self.mydict[node.key]
        self.length -= 1
    
    def insert(self, node):
        
        left = self.tail.prev
        right = self.tail
        
        left.next = node
        node.prev = left
        
        right.prev = node
        node.next = right
        
        self.length += 1
        self.mydict[node.key] = node
    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
