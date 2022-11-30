# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next; # make a copy of the next node 

        node.val = nextNode.val; # change the value of the current node to that of the next node 

        node.next = nextNode.next; # set the next value of the current node to that of the next node
        
        # idea: overwrite the current node with the values of the next node & skip the next node