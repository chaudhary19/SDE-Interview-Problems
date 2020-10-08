class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        

    def push(self, x):
        
        if(x <= self.min):
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
        

    def pop(self):
        
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()
        

    def top(self):
        
        return self.stack[-1]
        

    def getMin(self):
        
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
