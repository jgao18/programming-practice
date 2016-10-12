#https://codelab.interviewbit.com/problems/num1bits/
import math
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        numOnes = 0;
        for i in range(32, -1, -1):
            if 2**i <= A:
                numOnes += 1
                A = A - 2**i
        return numOnes
