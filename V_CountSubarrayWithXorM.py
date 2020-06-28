from collections import defaultdict

class Solution(object):
    def CountSubarraywithXortarget(self, Arr, target):
        
        length = len(Arr)
        preXor = 0
        hashmap = defaultdict(int)
        hasmap[0] = 1
        ans = 0
        
        for i in range(length):
        
            preXor ^= Arr[i]
            if preXor^target in hashmap:
                ans += hashmap[preXor ^ target]
            
            hashmap[preXor] += 1
        return ans
        
        
"""

Things to remember:

1) maintain a preXor which tells Xor upto current value in Array.
2) maintain a hashmap for count of xor occurences, initialize if {0: 1}
3) for ex - if curr element is 2 and target is 6, so we will find 2^6 = 4, is it present in hashmap or not?
3) if present, add the occurences in ans.
4) return the ans
"""
