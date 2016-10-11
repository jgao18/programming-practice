#https://www.hackerrank.com/challenges/ctci-comparator-sorting

# Pick a pivot element, and swap elements starting from either end comparing to a pivot /VALUE/
# move one pointer until something should be swapped, then move other until a swap is found
# repeat on two sorted sides

# ideally a good pivot is picked and the array is halved each time : O(nlogn) avg
# worst case- pivot is lowest elemnt in array O(n^2) 

# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.score = score
        self.name = name
        
    def __repr__(self):
        return name + str(self.score)
    
    def comparator(a, b):
        if (a.score == b.score):
            if (a.name < b.name):
                return -1
            else:
                return 1
        elif (a.score > b.score):
            return -1
        else:
            return 1
