class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ''
        
        mini = float('inf')
        for i in strs:
            mini = min(mini, len(i))
        
        prefix = ''
        for i in range(mini):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix
