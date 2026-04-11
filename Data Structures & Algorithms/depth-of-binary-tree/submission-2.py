# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        parent = [root]
        depth = 0

        while parent:
            depth += 1
            child = []

            for nodes in parent:
                if nodes.left:
                    child.append(nodes.left)
                if nodes.right:
                    child.append(nodes.right)

            parent = child[:]

        return depth

