class Solution(object):
    def nextGreaterElement(self, n):
        
        string = list(str(n))
        length = len(string)
        
        pos = length - 2
        while pos >= 0 and int(string[pos]) >= int(string[pos+1]):
            pos -= 1
        
        if pos < 0:        # case - 54321
            return -1
        
        j = length - 1
        while j > pos:
            if int(string[j]) > int(string[pos]):
                break
            j -= 1
        
        string[pos], string[j] = string[j], string[pos]
        
        left, right = pos + 1, length - 1
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
        
        return ''.join(string) if ((-2**31 - 1)<=int(''.join(string))<=(2**31 - 1)) else -1
                
        
