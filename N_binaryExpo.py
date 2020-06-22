class Solution(object):
    def myPow(self, x, n):
        
        def binpow(a, b):
            
            result = 1
            while b:
                if b&1:
                    result *= a
                    b -= 1
                else:
                    a *= a
                    b >>= 1
            return result
        
        ans = binpow(x, abs(n))
        if n<0:
            return 1/ans
        return ans
        
"""
1) works for positive and negative power too..
2) time complexity o(logn) iterations

"""
