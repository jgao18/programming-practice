#https://codelab.interviewbit.com/problems/lengthlast/
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        lastword = ''
        space = 0
        for letter in A:
            if letter != ' ':
                if space == 1:
                    lastword = ''
                space = 0
                lastword += letter
            else:
                space = 1
                
        if lastword == '':
            return 0
        else:
            return len(lastword)
