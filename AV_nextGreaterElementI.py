class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        
        mydict = {i: -1 for i in nums2}
        stack = []
        
        for i in nums2:
            while stack and stack[-1] < i:
                ele = stack.pop()
                mydict[ele] = i
            stack.append(i)
        
        ans = []
        for i in nums1:
            ans.append(mydict[i])
        return ans
