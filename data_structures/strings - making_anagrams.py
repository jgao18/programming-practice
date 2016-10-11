#https://www.hackerrank.com/challenges/ctci-making-anagrams

import string
def number_needed(a, b):
    numChars = 0
    for letter in string.ascii_lowercase:
        bCount = b.count(letter)
        aCount = a.count(letter)
        difference = abs(bCount - aCount)
        numChars += difference
    return numChars
            

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

  
