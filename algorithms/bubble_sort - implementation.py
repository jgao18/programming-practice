#https://www.hackerrank.com/challenges/ctci-bubble-sort
# O(n^2)
# Loop through each item, swap if out of order, keep going until end of items, 

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

totalSwaps = 0
for number in a:
    localSwaps = 0 
    for i in range(len(a) - 1):
        if (a[i] > a[i+1]):
            store = a[i]
            a[i] = a[i+1]
            a[i+1] = store
            totalSwaps += 1
            localSwaps += 1
    if localSwaps == 0:
        break

print "Array is sorted in " + str(totalSwaps) + " swaps."
print "First Element: " + str(a[0])
print "Last Element: " + str(a[-1])
