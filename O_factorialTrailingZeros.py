class Solution(object):

    def trailingZeroes(self, n):
        
        ans = 0                # for counting zeroes
        while n >= 5:
            ans += n//5
            n //= 5
        
        return ans
 
"""

1) complexity : O(log5n)
2) 100/5 + 20/5 + 4/5 = total no. of zeroes in 100!
3) divide by 5 untill the number becomes zero

"""
