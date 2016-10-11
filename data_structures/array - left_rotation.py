# https://www.hackerrank.com/challenges/ctci-array-left-rotation

'''
Array - (java) int[] array = new int[10] fixed length

Python only unlimited length;

Resizable - if full, create a new array with double space and copy over (adding still constant time)
'''

# n - number of integers
# k - number of left rotations
# a - array
def array_left_rotation(a, n, k):
    move = a[:k]
    a = a[k:]
    a += move
    
    a = [str(i) for i in a]
    print ' '.join(a)

        

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))



#too slow
'''
def array_left_rotation(a, n, k):
    while (k > 0):
        store = a[0]
        a = a[1:]
        a.append(store)
        k -= 1
    output = ''
    for item in a:
        output += str(item) + " "
    output = output[:-1]
    print output'''
  
