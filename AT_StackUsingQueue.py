from collections import deque

class MyStack(object):

    def __init__(self):
        
        self.Queue = deque()
        self.length = 0
        

    def push(self, x):
        
        self.Queue.append(x)
        self.length += 1
        for i in range(self.length - 1):
            self.Queue.append(self.Queue.popleft())
        

    def pop(self):
        self.length -= 1
        return self.Queue.popleft()

    def top(self):
        return self.Queue[0]
        

    def empty(self):
        return self.length == 0 
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
