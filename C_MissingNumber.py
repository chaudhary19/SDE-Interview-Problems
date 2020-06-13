class Solution(object):
    def missingNumber(self, nums):
        
        length = len(nums)
        res = 0
        for i in range(length):
            res^=(i+1)
            res^=nums[i]
        return res
        
"""

Things to remember:

1) do xor of all elements with indexes
2) another way : using summation of all the elements

"""
