class Solution(object):
    def myAtoi(self, s):
        
        S = list(s.strip())
        if len(S) == 0: return 0
        
        sign = -1 if S[0] == '-' else 1
        if S[0] in ['-', '+']: del S[0]
        
        result = i = 0
        while i < len(S) and S[i].isdigit():
            result = result * 10 + (ord(S[i]) - ord('0'))
            i += 1
        
        return max(-2**31, min(2**31 - 1, sign * result))
        
  # ATOI
        
