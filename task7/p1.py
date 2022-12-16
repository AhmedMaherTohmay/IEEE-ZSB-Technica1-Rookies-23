# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      # creating duumy list
        tail = dummy            
        while l1 and l2:        
            if l1.val < l2.val:   # comparing each number in the lists 
                tail.next = l1    # then assigning the small value to tail
                l1 = l1.next      # jumping to the next value 
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next       # making sure to update the tail

        if l1:                  # if one of the lists is empty and the other is not 
            tail.next = l1      # then we should skip the empty one and take the
        elif l2:                # the values of the other one 
            tail.next = l2

        return dummy.next
                
