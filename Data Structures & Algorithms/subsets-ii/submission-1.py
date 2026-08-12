class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        subset = []
        nums.sort()


        def dfs(idx):

            if idx == len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[idx])
            dfs(idx + 1)
            subset.pop()

            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(idx + 1)


        dfs(0)

        return ans


        