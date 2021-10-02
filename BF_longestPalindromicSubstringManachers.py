class Solution(object):
    def longestPalindrome(self, s):
        
        string = list(s)
        T = '$#'+'#'.join(string)+'#@'
        length = len(T)
        P = [0]*length
        
        center = right = 0
        
        for i in range(1, length-1):
            
            mirror = 2*center - i
            
            if i < right:
                P[i] = min(right-i, P[mirror])
            
            while T[i+(P[i]+1)]==T[i-(P[i]+1)]:
                P[i] += 1
            
            if i+P[i] > right:
                right = i+P[i]
                center = i
            
        maxlen, max_center = max((value, index) for index, value in enumerate(P))
        return s[(max_center-maxlen)//2 : (max_center+maxlen)//2]
        
        # Time Complexity: O(n)
        # space complexity: O(n)
