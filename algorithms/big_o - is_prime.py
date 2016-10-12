#https://www.hackerrank.com/challenges/ctci-big-o

import math

p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    
    if (n == 1):
        print "Not prime"
    else:
        bit = 0
        endRange = round(math.sqrt(n))
        for i in range(2, int(endRange)):
            divided = float(n)/float(i)
            if divided.is_integer():
                bit = 1
                print "Not prime"
                break

        if bit == 0:
            print "Prime"
