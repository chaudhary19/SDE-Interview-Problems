class Solution(object):
    def generate(self, numRows):
        
        ans = [[1]*i for i in range(1, numRows+1)]
        for i in range(1, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
        
        return ans
        
"""

Things to remember:

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

1) use summation: pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
2) initialize pascal matrix with 1 for easy implementation.

"""
