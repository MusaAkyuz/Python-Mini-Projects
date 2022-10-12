# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        '''
        Mission
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).

        A valid BST is defined as follows:

        + The left subtree of a node contains only nodes with keys less than the node's key.
        + The right subtree of a node contains only nodes with keys greater than the node's key.
        + Both the left and right subtrees must also be binary search trees.
        '''

        inf = sys.maxint

        def helper(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            # node.left must be smaller than node.value and bigger than -inf
            # node right must be bigger than node.value and smaller than inf
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        # inf mean infinity
        # root must be bigger than -inf and smaller than inf
        return helper(root, -inf, inf)

