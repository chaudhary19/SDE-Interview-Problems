class Solution(object):
    
    def solve(self, n, target, nums):
        
        dp = [[False for i in range(target+1)] for j in range(2)]
        
        for i in range(n+1):
            for j in range(target+1):
                
                if j == 0:
                    dp[i%2][j] = True
                elif i == 0:
                    dp[i][j] = False
                elif nums[i-1] <= j:
                    dp[i%2][j] = dp[(i+1)%2][j] or dp[(i+1)%2][j-nums[i-1]]
                else:
                    dp[i%2][j] = dp[(i+1)%2][j]
        return dp[n%2][target]
    
    def canPartition(self, nums):
        
        length = len(nums)
        Sum = sum(nums)
        
        if Sum&1:
            return False
        else:
            return self.solve(length, Sum//2, nums)
            
 # ------------------------------------------------------------------------------------------------------------
 
 class Solution(object):
    
    def solve(self, n, target, nums):
        
        dp = [[False for i in range(target+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
            
        for i in range(1, n+1):
            for j in range(1, target+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]
    
    def canPartition(self, nums):
        
        length = len(nums)
        Sum = sum(nums)
        if Sum&1:
            return False
        else:
            return self.solve(length, Sum//2, nums)
        
        
 # --------------------------------------------------------------------------------------------------------------
 
 class Solution(object):
    
    def solve(self, n, target, nums, memo):
        
        if target == 0:
            return True
        if n == 0:
            return False
        if (n, target) in memo:
            return memo[(n, target)]
        
        if nums[n-1] <= target:
            memo[(n, target)] = self.solve(n-1, target-nums[n-1], nums, memo) or self.solve(n-1, target, nums, memo)
        else:
            memo[(n, target)] = self.solve(n-1, target, nums, memo)
        
        return memo[(n, target)]
    
    def canPartition(self, nums):
        
        length = len(nums)
        Sum = sum(nums)
        
        if Sum&1:
            return False
        else:
            memo = dict()
            return self.solve(length, Sum//2, nums, memo)
        
