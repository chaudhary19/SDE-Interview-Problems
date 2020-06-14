
class Solution(object):
    
    def reversePair(self, nums):
        
        def mergeSort(nums):             # merge sort helper
            
            inv_count = 0
            if len(nums) > 1:
                mid = len(nums) / 2          # divide array into two equal length parts
                left = nums[:mid]
                right = nums[mid:]
                
                inv_count += mergeSort(left)
                inv_count += mergeSort(right)
                
                i = j = k = 0                           # merge the two sorted parts
                while i<len(left) and j<len(right):
                    if left[i] < right[j]:
                        nums[k] = left[i]
                        i += 1
                    else:
                        nums[k] = right[j]
                        j += 1
                    k += 1
                while i<len(left):
                    nums[k] = left[i]
                    i += 1
                    k += 1
                while j<len(right):
                    nums[k] = right[j]
                    j += 1
                    k += 1
            return inv_count                  # return the inversion count
        
        count = mergeSort(nums)
        return count
        
"""

Things to remember:
1) Take help of merge sort to find the count of total inversions in O(nlogn).
2) Time Complexity : O(nlogn).

"""
