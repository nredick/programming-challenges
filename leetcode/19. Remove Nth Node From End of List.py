from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use two offset pointers, such that when the first pointer reaches the end, the second pointer is at the node to remove 
        front, lag = head, head 
        # move the front pointer "ahead" by n nodes 
        for _ in range(n):
            front = front.next 
        if not front: # front reached the end already => node to remove is the first node 
            return head.next # return head without the first node 
        # move both pointers until the front pointer reaches the end 
        while front.next != None: 
            front = front.next
            lag = lag.next 
        # skip the nth node from the end 
        lag.next = lag.next.next 
        return head # return the modified linked list 