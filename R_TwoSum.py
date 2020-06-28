class Solution(object):

    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
            
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
                
"""
Things to remember:

1) Keep in your mind that given array is not sorted.
2) for ex - our target is 7, so if we get 2 at index 1, we will store (7 - 2) = 5 with index 1 as key in dictionary

"""
