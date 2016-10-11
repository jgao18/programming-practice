# https://www.hackerrank.com/challenges/ctci-ransom-note

def ransom_note(magazine, ransom):    
    if (len(ransom) > len(magazine)):
        return False
    
    for word in ransom:
        if (word not in magazine):
            return False
        else:
            magazine.remove(word)
    
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    
