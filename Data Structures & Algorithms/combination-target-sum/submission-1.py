class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        ans = []
        pile = []

        def dfs(idx, remaining):
            
            if remaining < 0 or idx == len(nums):
                return

            if remaining == 0:
                ans.append(pile.copy())
                return

            
            pile.append(nums[idx])
            dfs(idx, remaining - nums[idx])
            pile.pop()


            dfs(idx + 1, remaining)


        dfs(0, target)
        
        return ans
           
        