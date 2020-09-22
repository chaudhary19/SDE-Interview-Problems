class Solution(object):
    def longestOnes(self, nums, k):
        
        ans = start = zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                while zero > k:
                    if nums[start] == 0:
                        zero -= 1
                    start += 1
            ans = max(ans, i - start + 1)
        return ans
