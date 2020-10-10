# here we are implementing Manacher's Algorithm
# it can be used to find the length of longest Palindromic Substring
# it can be used to print the longest Palindromic Substring
# it can be used to find the count of all palindromic substring in a string

def longestPalindromicLength(string):
   
    string = list(string)
    T = '$#' + '#'.join(string) + '#@'
    length = len(T)
    P = [0]*length
    
    center = right = ans = 0
    
    for i in range(1, length - 1):
        
        mirror = 2 * center - i
        
        if i < right:
            P[i] = min(P[mirror], right - i)
        
        while T[i+(P[i]+1)] == T[i-(P[i]+1)]:
            P[i] += 1
        
        ans = max(ans, P[i])
        
        if i+P[i] > right:
            right = i+P[i]
            center = i
    return ans
    

def longestPalindromicSubstring(string):
    
    string = list(string)
    T = '$#' + '#'.join(string) + '#@'
    length = len(T)
    P = [0]*length
    
    center = right = 0
    for i in range(1, length-1):
        
        mirror = 2 * center - i
        
        if i < right:
            P[i] = min(P[mirror], right - i)
        
        while T[i+(P[i]+1)] == T[i-(P[i]+1)]:
            P[i] += 1
        
        if i+P[i] > right:
            right = i + P[i]
            center = i
    
    max_value, max_center = max([(value, index) for index, value in enumerate(P)])
    # print(max_value, max_center)
    return ''.join(string[(max_center - max_value)//2: (max_center + max_value)//2])


def countAllPalindromeString(string):
    
    string = list(string)
    T = '$#' + '#'.join(string) + '#@'
    length = len(T)
    P = [0]*length
    
    center = right = ans = 0
    
    for i in range(1, length - 1):
        
        mirror = 2 * center - i
        
        if i < right:
            P[i] = min(P[mirror], right - i)
        
        while T[i+(P[i]+1)] == T[i-(P[i]+1)]:
            P[i] += 1
        
        ans += (P[i] + 1)//2
        
        if i + P[i] > right:
            right, center = i + P[i], i
    
    return ans

def main():
    
    string = input()
    max_length = longestPalindromicLength(string)
    print(max_length)
    
    longestString = longestPalindromicSubstring(string)
    print(longestString)
    
    countPalindrome = countAllPalindromeString(string)
    print(countPalindrome)

if __name__ == "__main__":
    main()
