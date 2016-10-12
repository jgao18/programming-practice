#https://codelab.interviewbit.com/problems/gcd/

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        # Base Case
        if (A == B):
            return A
           
        #recurse 
        if (A > B):
            big = A
            small = B
        else:
            big = B
            small = A
            
        return self.gcd(big - small, small)


'''
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a
'''
