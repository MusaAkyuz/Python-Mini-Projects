"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        '''
        Mission
        Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
        Nary-Tree input serialization is represented in their level order traversal. 
        Each group of children is separated by the null value (See examples)
        '''

        if root is None: return []

        # creating result list and stack list
        # stack for temp list to manipulate
        # stack store nodes
        res = []
        stack = [root]

        # while stack is empty
        while stack:

            # deleting last node from stack and keeping on temp variable
            temp = stack.pop()
            # appending for result
            res.append(temp.val)
            # creating new stack but reverse order
            # so we can delete every time last node
            # and we can add every time their chiled reverse
            stack.extend(temp.children[::-1])
        return res
