class Solution(object):
    def romanToInt(self, s):
        
        ans = 0
        value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        for i in range(len(s) - 1):
            if value[s[i]] < value[s[i+1]]:
                ans -= value[s[i]]
            else:
                ans += value[s[i]]
        ans += value[s[-1]]
        return ans
        
