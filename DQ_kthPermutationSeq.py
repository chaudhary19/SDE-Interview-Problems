class Solution(object):
    def getPermutation(self, n, k):
        
        fact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = i * fact[i-1]
        
        ans = []
        nums = range(1, n+1)
        k -= 1
        
        while n > 0:
            n -= 1
            index = k // fact[n]
            k = k % fact[n]
            ans.append(str(nums[index]))
            # nums.remove(nums[index])
            del nums[index]
        
        return ''.join(ans)
        
