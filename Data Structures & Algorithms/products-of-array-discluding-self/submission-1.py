class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []
        
        running_product = 1
        for num in nums:
            ans.append(running_product)
            running_product *= num

        running_product = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= running_product
            running_product *= nums[i]


        return ans

            
            
        
        

