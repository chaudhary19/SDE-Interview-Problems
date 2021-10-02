
def partial(pattern):
    
    g = 0
    length = len(pattern)
    pi = [0]*length
    
    for i in range(1, length):
        while g and (pattern[i] != pattern[g]):
            g = pi[g-1]
        pi[i] = g = g + (pattern[i] == pattern[g])
    
    return pi


def isPresent(string, pattern):
    
    pi = partial(pattern)
    
    g = 0
    for i in range(len(string)):
        while g and (string[i] != pattern[g]):
            g = pi[g-1]
        g += (string[i] == pattern[g])
        if g == len(pattern):
            return True
    return False


def findIndexes(string, pattern):
    
    pi = partial(pattern)
    g = 0
    idx = []
    
    for i in range(len(string)):
        while g and (string[i] != pattern[g]):
            g = pi[g-1]
        g += (string[i] == pattern[g])
        if g == len(pattern):
            idx.append(i-g+1)
            g = pi[g-1]
    return idx


def main():
    
    string = input()
    pattern = input()
    
    if isPresent(string, pattern):
        print(pattern, " is present in ", string)
        idx = findIndexes(string, pattern)
        print(idx)
    
    else:
        print(pattern, " is not present in ", string)
    
    
if __name__ == "__main__":
    main()
