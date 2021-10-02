class Solution(object):
    def countAndSay(self, n):
        
        def fxn(s):
            
            s += '#'
            count = 1
            curr = s[0]
            ans = []
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    ans.append(str(count))
                    ans.append(curr)
                    count = 1
                    curr = s[i]
            return ''.join(ans)
                    
        
        start = '1'
        for i in range(n-1):
            start = fxn(start)
        return start
        
