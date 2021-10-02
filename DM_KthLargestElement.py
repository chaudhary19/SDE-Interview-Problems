# different methods to do this problem
# direct sorting and return kth element - O(nlogn)
# using heap - O(nlogk)
# using Quick Sort - best O(n) and worst(n^2)

class Solution(object):
    
    def findKthSmallest(self, nums, k):
        return self.QuickSort(nums, 0, len(nums) - 1, k)
    
    def QuickSort(self, nums, start, end, k):
        
        if start <= end:
            
            pivot = self.partition(nums, start, end)
            
            if k < pivot+1:
                return self.QuickSort(nums, start, pivot-1, k)
            elif k > pivot+1:
                return self.QuickSort(nums, pivot+1, end, k)
            else:
                return nums[pivot]
    
    def partition(self, nums, start, end):
        
        l, r, low = start, end, start
        
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        
        nums[r], nums[low] = nums[low], nums[r]
        return low
    
    def findKthLargest(self, nums, k):
        return self.findKthSmallest(nums, len(nums) - k + 1)    
