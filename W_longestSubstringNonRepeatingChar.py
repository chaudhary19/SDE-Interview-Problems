class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        mydict = dict()
        maxi = start = 0
        
        for i in range(len(s)):
            
            mydict[s[i]] = mydict.get(s[i], 0) + 1
            
            while mydict[s[i]]>1:
                if mydict[s[start]]>1:
                    mydict[s[start]] -= 1
                else:
                    del mydict[s[start]]
                start += 1
            
            maxi = max(maxi, i-start+1)
        
        return maxi
        
"""

Things to remember:
1) maintain a hashmap of characters in current substring.
2) use two pointers to represent the current substring.
3) Time Complexity: O(n)
$) Space Complexity: O(n)

"""
