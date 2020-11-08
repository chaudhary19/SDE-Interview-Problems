class Solution(object):
    def combinationSum2(self, candidates, target):
        
        self.ans = []
        candidates.sort()
        
        self.dfs([], target, 0, candidates)
        return self.ans
    
    def dfs(self, temp, remain, index, candidates):
        
        if remain < 0:
            return
        elif remain == 0:
            self.ans.append(temp)
            return
        else:
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                self.dfs(temp+[candidates[i]], remain-candidates[i], i+1, candidates)
