# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        '''
        Misison
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists in a one sorted list. The list should be made by 
        splicing together the nodes of the first two lists.
        Return the head of the merged linked list.
        '''

        # converting linked list to list
        cList1 = []
        cList2 = []

        current = list1
        while current != None:
            cList1.append(current.val)
            current = current.next

        current = list2
        while current != None:
            cList2.append(current.val)
            current = current.next  

        # merging two list and sorted
        sortedList = sorted(cList1 + cList2)

        # reconverting linked list
        # creating linked list
        lList = ListNode()

        # creating temp new node 
        current = lList
        for item in sortedList:
            # append to new linked List
            while current.next:
                current = current.next
            current.next = ListNode(item)
        
        # deleting first item which 0"zero"
        temp = lList
        lList = lList.next
        temp = None

        return lList