from typing import * 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # idea: iterate over the list, making the current node point at the previous 
        # when end of the list is reached, return that node, which has become the head 
        prev = None 
        
        while head: # iterate to the end of the singly linked list 
            next = head.next; # store the next node 
            head.next = prev; # set the next node to the previous node 
            prev = head; # set the previous node to the current node 
            head = next; # set the current node to the stored next node 
            
        return prev # return the reversed list 