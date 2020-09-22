class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        
        zero = start = ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                while zero > 1:
                    if nums[start] == 0:
                        zero -= 1
                    start += 1
            ans = max(ans, i - start + 1)
        return ans
