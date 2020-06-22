class Solution(object):
    
    def gcd(self, a, b):
        
        while b:
            a, b = b, a%b
        return a

"""
1) Time Complexity : O(log(min(a, b))

"""
