class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        left_max = [0] * n
        running_max = 0

        for idx in range(n):
            left_max[idx] = running_max
            running_max = max(height[idx],running_max)


        right_max = [0] * n
        running_max = 0

        for idx in range(n - 1, -1, -1):
            right_max[idx] = running_max
            running_max = max(height[idx],running_max)


        ans = 0

        for i in range(len(height)):

            water = min(left_max[i], right_max[i]) - height[i]

            if water > 0:
                ans += water

        return ans














        