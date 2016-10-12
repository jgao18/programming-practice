# https://codelab.interviewbit.com/problems/remduplnk/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        itOne = A
        itTwo = A.next
        while itTwo is not None:
            if itOne.val == itTwo.val:
                itTwo = itTwo.next
                itOne.next = itTwo
            else:
                itOne = itOne.next
                itTwo = itTwo.next
        return head
        
            

  
