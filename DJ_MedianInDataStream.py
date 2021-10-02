from heapq import heappush, heappop, heappushpop, heapify

class MedianFinder(object):

    def __init__(self):
        
        self.small = []             # max heap 
        self.large = []             # min heap
        

    def addNum(self, num):
        
        heappush(self.small, -heappushpop(self.large, num))
        if len(self.small) > len(self.large):
            heappush(self.large, -heappop(self.small))
        

    def findMedian(self):
        
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
