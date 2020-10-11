class Solution(object):
    
    def partial(self, s):
        
        g = 0
        length = len(s)
        pi = [0]*length
        
        for i in range(1, length):
            while g and (s[i] != s[g]):
                g = pi[g-1]
            pi[i] = g = g + (s[i] == s[g])
        
        return pi
    
    def shortestPalindrome(self, s):
        
        n = len(s)
        temp = s + '$' + ''.join(reversed(list(s)))
        
        pi = self.partial(temp)
        ans = n - pi[-1]
        
        s = s[-1: -ans-1: -1] + s
        return s
