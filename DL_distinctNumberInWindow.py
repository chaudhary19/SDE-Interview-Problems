from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        
        n = len(A)
        ans = []
        if B > n:
            return ans
        
        mydict = defaultdict(int)
        for i in range(B):
            mydict[A[i]] += 1
        
        length = len(mydict)
        ans.append(length)
        
        for i in range(B, n):
            ele = A[i - B]
            if mydict[ele] > 1:
                mydict[ele] -= 1
            else:
                del mydict[ele]
                length -= 1
            
            new_ele = A[i]
            if new_ele in mydict:
                mydict[new_ele] += 1
            else:
                mydict[new_ele] = 1
                length += 1
            ans.append(length)
        
        return ans
        
        
