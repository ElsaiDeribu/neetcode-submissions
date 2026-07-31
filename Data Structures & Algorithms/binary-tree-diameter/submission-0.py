# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        def dfs(node):
            if not node: return 0, 0

            left_longest, left_straight = dfs(node.left)
            right_longest, right_straight = dfs(node.right)

            longest = max(left_straight + right_straight, left_longest, right_longest)

            return longest, max(left_straight, right_straight) + 1


        return dfs(root)[0]


