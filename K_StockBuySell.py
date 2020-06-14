# using kadane's algorithm

class Solution(object):
    def maxProfit(self, prices):
        
        maxCurr = maxSoFar = 0
        
        for i in range(1, len(prices)):
            maxCurr = max(0, maxCurr + prices[i] - prices[i-1])
            maxSoFar = max(maxCurr, maxSoFar)
        
        return maxSoFar
        
"""

Things to remember:
1) think price array as of Difference array
2) let p = [a0, a1, a2, a3, a4, a5, a6, a7]
3) let diff = [b0, b1, b2, b3, b4, b5, b6, b7]

    b0 = 0
    b1 = a1 - a0
    b2 = a2 - a1
    b3 = a3 - a2
    b4 = a4 - a3
    b5 = a5 - a4
    b6 = a6 - a5
    b7 = a7 - a6
    
    let a6 - a2 = max difference
    hence, b3 + b4 + b5 + b6 = a6 - a2
    That's why kadane's algo works here.
    

"""
