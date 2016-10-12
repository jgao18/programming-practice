#https://codelab.interviewbit.com/problems/mice/
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, mice, holes):
        mice.sort()
        holes.sort()
        
        maxVal = float("-inf")
        
        for i in range(len(mice)):
            time = abs(mice[i] - holes[i])
            if time > maxVal:
                maxVal = int(time)
        
        return maxVal
                
