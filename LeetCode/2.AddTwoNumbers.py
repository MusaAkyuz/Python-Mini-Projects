# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        """
        Mission
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        """

        num1 = 0
        num2 = 0

        multiple = 1
        while l1:
            num1 += (l1.val * multiple)
            l1 = l1.next
            multiple *= 10

        multiple = 1
        while l2:
            num2 += (l2.val * multiple)
            l2 = l2.next
            multiple *= 10

        total = num1 + num2
        total = str(total)

        resList = []
        for _ in total:
            resList.insert(0, int(_))

        # reconverting linked list
        # creating linked list
        lList = ListNode()

        # creating temp new node 
        current = lList
        for item in resList:
            # append to new linked List
            while current.next:
                current = current.next
            current.next = ListNode(item)
        
        # deleting first item which 0"zero"
        temp = lList
        lList = lList.next
        temp = None

        return lList
        