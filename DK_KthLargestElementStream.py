from heapq import heappush, heappop, heappushpop, heapify

class KthLargest(object):

    def __init__(self, k, nums):
        
        self.pool = nums
        self.k = k
        heapify(self.pool)
        while len(self.pool) > k:
            heappop(self.pool)

    def add(self, val):
        
        if len(self.pool) < self.k:
            heappush(self.pool, val)
        else:
            heappushpop(self.pool, val)
        return self.pool[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
