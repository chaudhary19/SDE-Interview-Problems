def z_function(string):
    
    n = len(string)
    Z = [0]*n
    l = r = 0
    
    for i in range(1, n):
        z = Z[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and string[z] == string[i + z]:
                z += 1
        
        Z[i] = z
    
    Z[0] = n
    return Z

def main():
    
    string = input()
    pattern = input()
    new_string = pattern + '$' + string
    z = z_function(new_string)
    print(z)
    
    for i in range(len(string)):
        k = z[i + len(pattern) + 1]
        if k == len(pattern):
            print('pattern found at ', i)
            
    

if __name__ == "__main__":
    main()
