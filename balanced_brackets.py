#https://www.hackerrank.com/challenges/ctci-balanced-brackets
def is_matched(expression):
    toMatch = []
    pairs = {'}':'{', ']':'[', ')':'('}
    for exp in expression:
        if len(toMatch) == 0:
            toMatch.append(exp)
        elif exp not in pairs.keys():
            toMatch.append(exp)
        else: 
            if pairs[exp] == toMatch[-1]:
                toMatch.pop()
    if len(toMatch) != 0:
        return False
    else:
        return True
        
        

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
