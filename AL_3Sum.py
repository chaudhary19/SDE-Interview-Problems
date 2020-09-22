class Solution(object):
    def threeSum(self, nums):
        
        nums.sort()
        ans, n, i = [], len(nums), 0
        while i<n:
            if nums[i]>0:   # three positive numbers can't give sum = 0
                break
            target = abs(nums[i])
            start, end = i+1, n-1
            while start<end:
                if nums[start]+ nums[end]==target:  # I got u
                    ans.append([nums[i], nums[start], nums[end]])
                    while start<end-1 and nums[start]==nums[start+1]:
                        start+=1
                    start+1
                    while start<end-1 and nums[end]==nums[end-1]:
                        end-=1
                    end-=1
                elif nums[start]+ nums[end] > target:
                    end -= 1
                else:
                    start += 1
            while i<(n-1) and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return ans
        
        
        
