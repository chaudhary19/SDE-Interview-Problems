class Solution(object):
    def largestRectangleArea(self, heights):
        
        ans = 0
        length = len(heights)
        stack = []
        
        for i in range(length):
            while stack and heights[stack[-1]] > heights[i]:
                curr = heights[stack.pop()]
                if stack:
                    ans = max(ans, (i - stack[-1] - 1) * curr)
                else:
                    ans = max(ans, i * curr)
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            curr = heights[idx]
            if stack:
                ans = max(ans, (length - stack[-1] - 1) * curr)
            else:
                ans = max(ans, (length) * curr)
        
        return ans
                
        
