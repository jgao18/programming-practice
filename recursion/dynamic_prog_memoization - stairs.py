#https://www.hackerrank.com/challenges/ctci-recursive-staircase

def recurse(num):
    # base cases:
    if num < 0:
        return 0
    
    elif num == 0:
        return 1
    
    return calculate(num-1) + calculate(num-2) + calculate(num-3)


def memo(num, memo):
    # base cases:
    if num < 0:
        return 0
    
    elif num <= 0:
        return 1
    
    if (num not in memo.keys()):
        memo[num] = calculate(num-1, memo) + calculate(num-2, memo) + calculate(num-3, memo)
    return memo[num]

def dp(num):
    # base cases:
    if num < 0:
        return 0
    
    elif num <= 1:
        return 1
    
    paths = [1,1,2]
    for i in range(3,num):
        paths.append(paths[i-1] + paths[i-2] + paths[i-3])
        
    return paths[num]

def iterative(num):
    # base cases:
    if num < 0:
        return 0
    
    elif num <= 1:
        return 1
    
    paths = [1,1,2]
    for i in range(3,num):
        paths[0] = paths[1]
        paths[1] = paths[2]
        paths[2] = paths[2] + paths[1] + paths[0]
        
    return paths[2]


s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print iterative(n)
    
