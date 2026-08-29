class Solution:
    def canJump(self, nums: List[int]) -> bool:


        curr_max = 0

        for i in range(len(nums) - 1):

            curr_max = max(nums[i], curr_max)
            curr_max -= 1

            if curr_max < 0:
                return False


        return True
        
        