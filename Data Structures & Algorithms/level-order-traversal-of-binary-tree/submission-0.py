# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        def dfs(node, h):
            if not node:
                return

            if len(ans) < h:
                ans.append([])

            ans[h - 1].append(node.val)
            
            dfs(node.left, h + 1)
            dfs(node.right, h + 1)

        dfs(root, 1)

        return ans

            

        