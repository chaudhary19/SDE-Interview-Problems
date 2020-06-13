class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        index = m+n-1
        n,m = n-1, m-1
        
        while index>=0 and n>=0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m-=1
                
            else:
                nums1[index] = nums2[n]
                n-=1
                
            index -= 1
            
        while index>=0 and n>=0:
            nums1[index] = nums2[n]
            index -= 1
            n -= 1
            
"""

Things to remember:

1) Start comparing the last elements of both sorted array
2) put the greater element at the last index
3) Again start comparing the elements
4) untill you finished up both arrays or reached the starting indexes.


"""
