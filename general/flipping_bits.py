#https://codelab.interviewbit.com/problems/bulbs/
class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        counter = 0
        for i in range(0, len(A)):
            if (counter % 2) == 0: # even counter means switch is original
                if A[i] == 0:
                    counter +=1
                    A[i] = 1
            else: # odd counter means switch should flipped
                if A[i] == 1: # odd counter means A[i] is actually 0 when 1
                    counter += 1
                    
        return counter
