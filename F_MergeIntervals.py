class Solution(object):
    def merge(self, intervals):
        
        ans = []
        for i in sorted(intervals):
            if ans and ans[-1][-1] >= i[0]:
                ans[-1][-1] = max(ans[-1][-1], i[1])
            else:
                ans.append(i)
        
        return ans
        

"""

Things to remember:
1) Sort the intervals according to the first parameter.
2) check if current interval starting timing is less than or equal to last one's end timing.
3) else append the current interval.

"""
