class Solution(object):
    def combinationSum(self, candidates, target):
        
        self.ans = []
        self.candidates = candidates
        self.candidates.sort()
        
        self.dfs([], target, 0)     # 0 ---> current index
        return self.ans
    
    def dfs(self, temp, remain, index):
        
        if remain < 0:
            return
        elif remain == 0:
            self.ans.append(temp)
            return
        else:
            for i in range(index, len(self.candidates)):
                self.dfs(temp+[self.candidates[i]], remain - self.candidates[i], i)
