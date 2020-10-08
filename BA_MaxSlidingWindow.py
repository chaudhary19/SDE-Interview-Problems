from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        
        n = len(nums)
        Q = deque()
        
        for i in range(k):
            while Q and nums[Q[-1]] < nums[i]:
                Q.pop()
            Q.append(i)
        
        ans = []
        for i in range(k, n):
            ans.append(nums[Q[0]])
            
            while Q and Q[0] <= (i - k):
                Q.popleft()
            
            while Q and nums[Q[-1]] < nums[i]:
                Q.pop()
            
            Q.append(i)
        
        ans.append(nums[Q[0]])
        return ans
        
        
