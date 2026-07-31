class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) == 1: return [1]

        pref = []
        post = []
        ans = []
        

        running_product = 1
        for num in nums:

            running_product *= num
            pref.append(running_product)
        
        running_product = 1
        for i in range(len(nums) - 1, -1, -1):
            running_product *= nums[i]
            post.append(running_product)

        post = post[::-1]
        for i in range(len(nums)):
            if i == 0:
                ans.append(post[1])
            elif i == (len(nums) - 1):
                ans.append(pref[-2])

            else:
                ans.append(pref[i - 1] * post[i + 1])

        return ans

            
            
        
        

