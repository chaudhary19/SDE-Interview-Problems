# We can make it k-general case simply :)

class Solution(object):
    def removeDuplicates(self, nums):
        
        index = 0
        for num in nums:
            if index<2 or nums[index-2] < num:
                nums[index] = num
                index += 1
        return index
