class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        ans = []
        pile = []

        def dfs(start, remaining):
            
            if remaining < 0:
                return

            if remaining == 0:
                ans.append(pile.copy())
                return


            for idx in range(start, len(nums)):

                pile.append(nums[idx])
                dfs(idx, remaining - nums[idx])
                pile.pop()

        dfs(0, target)
        
        return ans
           
        