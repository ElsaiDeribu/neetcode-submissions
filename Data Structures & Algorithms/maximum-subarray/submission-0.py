class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        running_min = 0
        running_sum = 0
        ans = float("-inf")

        for num in nums:
            running_sum += num
            ans = max(ans, running_sum - running_min )
            running_min = min(running_sum, running_min)


        return ans