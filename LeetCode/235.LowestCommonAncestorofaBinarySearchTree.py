# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        '''
        Mission
        Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

        According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes 
        p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a 
        descendant of itself).”
        '''

        # We accapted binary tree is correct and there is no test case return None needed
        while True:
            # if both p and q less than root, new root = root.left
            if p.val < root.val and q.val < root.val:
                root = root.left
            # if both p and q bigger than root, new root = root.right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # otherwise return root already
            else:
                return root
