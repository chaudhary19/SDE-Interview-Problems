# lets do this using KMP

class Solution(object):
    
    def partial(self, pattern):
        
        length = len(pattern)
        g = 0
        pi = [0]*length
        
        for i in range(1, length):
            while g and (pattern[i] != pattern[g]):
                g = pi[g-1]
            pi[i] = g = g + (pattern[i] == pattern[g])
        
        return pi
    
    def strStr(self, text, pattern):
        
        if not pattern:
            return 0
        
        pi = self.partial(pattern)
        g = 0
        
        for i in range(len(text)):
            while g and (pattern[g] != text[i]):
                g = pi[g-1]
            g += (pattern[g] == text[i])
            
            if g == len(pattern):
                return (i-g+1)
        return -1
        
        
