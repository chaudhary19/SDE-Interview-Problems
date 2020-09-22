class Solution(object):
    def isValid(self, string):
        
        mydict = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in string:
            if i not in mydict:
                stack.append(i)
            else:
                if not stack or stack[-1] != mydict[i]:
                    return False
                else:
                    stack.pop()
        return stack == []
