class Solution(object):
    def sortColors(self, Arr):
        
        zero = one = two = -1
        
        for i in range(len(Arr)):
        
            if Arr[i] == 0:
                two += 1
                Arr[two] = 2
                one += 1
                Arr[one] = 1
                zero += 1
                Arr[zero] = 0
            
            elif Arr[i] == 1:
                two += 1
                Arr[two] = 2
                one += 1
                Arr[one] = 1
            else:
                two += 1
                Arr[two] = 2
        
"""

Things to remeber:

1) initially all the pointers are pointing to -1
2) whenever you got 0, first increase two, then one and then zero.
3) similarly when you got 1, increase two first and then one.
4) just put all the larger numbers after smaller ones.
5) time complexity : O(n) single pass algorithm

"""
