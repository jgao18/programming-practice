# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor

# sorted array; compare value to midpoint; check left (smaller)
# or right side (greater); repeat2
#
# O(logn)

t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))

#m - money to spend
#n - number of flavors
#a - list of flavorts

original = []
for item in a:
    original.append(item)
    
a.sort()
purchases = []

start = 0
end = len(a) - 1

while (True):
    if (a[start] + a[end] == m):
        break
    elif (a[start] + a[end] > m):
        end -= 1
    else:
        start += 1

for i in range(len(original)):
    if (original[i] == a[start]) or (original[i] == a[end]):
        purchases.append(i + 1)
purchases.sort()
print ' '.join(map(str,purchases))
