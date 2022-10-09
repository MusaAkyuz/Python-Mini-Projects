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

        # empty list for solution
        result = []

        # using recursion
        self.preorderR(root, result)
        return result

    def preorderR(self, root, result):
        # if empty
        if not root:
            return

        # otherwise append to list the value
        result.append(root.val)
        
        # recursive part
        for item in root.children:
            self.preorderR(item, result)