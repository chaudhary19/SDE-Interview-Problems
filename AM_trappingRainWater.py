class Solution(object):
    def trap(self, height):
        
        length = len(height)
        left, right = 0, length - 1
        leftmax = rightmax = ans = 0
        
        while left <= right:
            
            if height[left] <= height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    ans += (leftmax - height[left])
                left += 1
            
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    ans += (rightmax - height[right])
                right -= 1
        return ans
                
