def search(pattern, text, q, d):
    
    m, n = len(pattern), len(text)
    p = t = i = j = 0
    h = 1
    
    for i in range(m-1):
        h = (h * d) % q
    
    # calculate hash value for the pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
        
    # find the match
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print("Pattern found at ", i+1)
        
        if i < n-m:
            t = (d*(t - ord(text[i])*h) + ord(text[i+m])) % q
            
            if t < 0:
                t += q
                

def main():
    
    text = input()
    pattern = input()
    q = 13                    # a prime number
    d = 10                    # a multiplier
    search(pattern, text, q, d)

if __name__ == "__main__":
    main()
    
