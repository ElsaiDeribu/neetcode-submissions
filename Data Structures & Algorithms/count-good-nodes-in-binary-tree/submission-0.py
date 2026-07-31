# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(node, rn_max):
            if not node: return 0

            temp = 0
            if node.val >= rn_max:
                temp = 1
                rn_max = node.val

            return dfs(node.left, rn_max) + dfs(node.right, rn_max) + temp



        return dfs(root, float("-inf"))
