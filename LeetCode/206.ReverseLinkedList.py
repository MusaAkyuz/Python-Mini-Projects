# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        '''
        Mission
        Given the head of a singly linked list, reverse the list, and return the reversed list.
        '''

        cList = []

        current = head
        while current != None:
            cList.append(current.val)
            current = current.next

        cList.reverse()

        # reconverting linked list
        # creating linked list
        lList = ListNode()

        # creating temp new node 
        current = lList
        for item in cList:
            # append to new linked List
            while current.next:
                current = current.next
            current.next = ListNode(item)
        
        # deleting first item which 0"zero"
        temp = lList
        lList = lList.next
        temp = None

        return lList