# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        '''
        Mission
        Given the head of a singly linked list, return the middle node of the 
        linked list. If there are two middle nodes, return the second middle node.
        '''
        
        # converting linked list to list
        cList1 = []
        middle = 0

        while head != None:
            middle += 1
            cList1.append(head.val)
            head = head.next
        print(middle)
        middle //= 2
        print(middle)
        cList1 = cList1[middle:]

        # reconverting linked list
        # creating linked list
        lList = ListNode()

        # creating temp new node 
        current = lList
        for item in cList1:
            # append to new linked List
            while current.next:
                current = current.next
            current.next = ListNode(item)
        
        # deleting first item which 0"zero"
        temp = lList
        lList = lList.next
        temp = None

        return lList