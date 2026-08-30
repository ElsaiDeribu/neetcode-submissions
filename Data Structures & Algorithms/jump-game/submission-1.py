class Solution:
    def canJump(self, nums: List[int]) -> bool:


        tank = 0

        for i in range(len(nums) - 1):

            tank = max(nums[i], tank)
            tank -= 1

            if tank < 0:
                return False


        return True
        
        