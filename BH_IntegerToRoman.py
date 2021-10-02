class Solution(object):
    def intToRoman(self, num):
        
        dict = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        ans = ''
        for letter, number in zip(dict, n):
            ans += letter*(num//number)
            num %= number
        return ans
        
