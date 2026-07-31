class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        curr_list = []
        visited = set()

        def dfs():

            if len(curr_list) == len(nums):
                ans.append(curr_list.copy())
                return


            for i in range(len(nums)):
                if nums[i] not in visited:
                    curr_list.append(nums[i])
                    visited.add(nums[i])
                    dfs()
                    visited.remove(nums[i])
                    curr_list.pop()


        dfs()

        return ans