class Solution(object):
    def findDuplicate(self, nums):
        
        if len(nums) > 1:    # else no cycle will be present
            
            slow = nums[0]             
            fast = nums[nums[0]]
            
            while slow != fast:     # first find is cycle present?
                slow = nums[slow]
                fast = nums[nums[fast]]
            
            fast = 0
            while slow != fast:     # now find the first node of cycle
                slow = nums[slow]
                fast = nums[fast]
            
            return slow
        
        return -1
        
"""
Things to remeber:

1) if length <= 1, not possible to have a cycle or duplicate node.
2) use Floyd technique to find cycle by using slow and fast pointer.
3) Initially check whether cycle is present or not?
4) If cycle is present then find out the first node.

"""
