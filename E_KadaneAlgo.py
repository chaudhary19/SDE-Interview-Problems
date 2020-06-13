# kadane's algorithm

class Solution(object):
    def maxSubArray(self, nums):
        
        currSum = 0
        maxSum = -float('inf')
        for i in nums:
            currSum = max(currSum+i, i)
            maxSum = max(maxSum, currSum)
        return maxSum
        
"""

Things to remember:
1) for each element, check what is maximum --- curr element or sum of curr element and currSum
2) for each step, check the maximum Sum we can achieve.


"""
