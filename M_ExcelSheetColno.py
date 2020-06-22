class Solution(object):

    def titleToNumber(self, s):
    
        mydict = {chr(i) : i-64 for i in range(65,91)}
        curr, ans = 0, 0 
        for i in s[::-1]:
            ans += mydict[i]*pow(26,curr)
            curr += 1
        return ans
        
"""
AB --> 28
ABC ---> 26^2 x mydict[A]  +  26^1 x mydict[B] + 26^0 x mydict[C]

mydict = {A : 1, B : 2, C : 3............. Z : 26}

"""
