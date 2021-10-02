class Solution(object):
    
    def isPal(self, s):
        return s == s[::-1]
    
    def partition(self, s):
        self.ans = []
        self.dfs([], s)
        return self.ans
    
    def dfs(self, temp, s):
        
        if not s:
            self.ans.append(temp)
        else:
            for i in range(1, len(s)+1):
                if self.isPal(s[:i]):
                    self.dfs(temp+[s[:i]], s[i:])
        
        
