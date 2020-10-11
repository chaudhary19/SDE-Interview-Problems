class Solution(object):
    def isAnagram(self, s, t):
        
        mydict1, mydict2 = {}, {}
        
        for i in s:
            mydict1[i] = mydict1.get(i, 0) + 1
        for i in t:
            mydict2[i] = mydict2.get(i, 0) + 1
        
        return mydict1 == mydict2
