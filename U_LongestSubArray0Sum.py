class Solution(Object):
    def longestSubarrayZeroSum(self, Arr):
        
        curr = 0
        length = len(Arr)
        hashmap = dict()
        maximum = 0
        
        for i in range(length):
            curr += Arr[i]
            if curr == 0:
                maximum = max(maximum, i + 1)
            elif curr in hashmap:
                maximum = max(maximum, i - hashmap[curr])
            else:
                hashmap[curr] = i
        return maximum
        
"""

Things to remember:
1) store the first index of curr in hashmap
2) add current element of Array in curr for each iteration
3) check if curr is already present in hashmap or not?
4) if presnet, compare the distance with maximum.

"""
            
        
    
