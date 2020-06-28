class Solution(object):
    def longestConsecutive(self, nums):
        
        nums = set(nums)
        max_length = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                max_length = max(max_length, y - x)
        return max_length

"""
Things to remember:

1) Time Complexity: O(n)
2) Space Complexity: O(n)

"""
