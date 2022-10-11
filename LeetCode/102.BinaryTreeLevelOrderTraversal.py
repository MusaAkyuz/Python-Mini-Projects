# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """


        '''
        Mission
        Given the root of a binary tree, return the level order traversal of its nodes' values. 
        (i.e., from left to right, level by level).

 
        '''

        # is empty return []
        if root is None: return []

        # deque -> doubly enden query
        # we can add to right or left or pop from right or left
        queue = collections.deque([root]) 
        # result list
        res = []

        # until ends the pop
        while queue:
            size = len(queue)
            tmp=[]
            while size>0: 
                # starting with left node which first root
                # we are popping so deleting from queue
                node = queue.popleft()
                # appanding to temp
                tmp.append(node.val)
                # first, trying left side
                if node.left:
                    queue.append(node.left)
                # after, trying right side
                if node.right:
                    queue.append(node.right)
                size-=1
            res.append(tmp)
        return res
        