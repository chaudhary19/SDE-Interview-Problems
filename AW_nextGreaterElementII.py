class Solution(object):
    def nextGreaterElements(self, nums):
        
        store = nums + nums
        length = len(store)
        ans = [-1]*length
        stack = []
        
        for i in range(length):
            
            while stack and store[stack[-1]] < store[i]:
                ans[stack.pop()] = store[i]
            stack.append(i)
        
        return ans[:length//2]
