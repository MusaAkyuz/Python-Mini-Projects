# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        '''
        Mission
        Given the head of a linked list, return the node where the cycle begins. 
        If there is no cycle, return null.
        There is a cycle in a linked list if there is some node in the list that 
        can be reached again by continuously following the next pointer. 
        Internally, pos is used to denote the index of the node that tail's 
        next pointer is connected to (0-indexed). It is -1 if there is no cycle. 
        Note that pos is not passed as a parameter.
        Do not modify the linked list.
        '''

        # lookup for checks loop
        current = head
        lookup = set()

        # if there is no loop in linked list
        # return None
        while current:
            # if there is any same data in linked list
            # there is cycle
            if current in lookup:
                return current
            lookup.add(current)
            current = current.next
        return None