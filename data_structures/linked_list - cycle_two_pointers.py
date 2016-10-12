# https://codelab.interviewbit.com/problems/listcycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        nodeOne = A
        nodeTwo = A
        
        if ( (A is None) or (A.next is None) ):
            return None
        
        isCycle = False
        while( (nodeOne is not None) and (nodeTwo is not None) ):
            nodeOne = nodeOne.next
            
            if (nodeTwo.next is None):
                return None
            nodeTwo = nodeTwo.next.next
            
            if (nodeOne == nodeTwo):
                isCycle = True
                break
        
        if isCycle == True:
            nodeOne = A
            
            while(True):
                if (nodeOne == nodeTwo):
                    return nodeOne
                else:
                    nodeOne = nodeOne.next
                    nodeTwo = nodeTwo.next
        else:
            return None
        
        



'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        reached = []
        while A is not None:
            if A in reached:
                return A
            else:
                reached.append(A)
            A = A.next
        return None   
'''

