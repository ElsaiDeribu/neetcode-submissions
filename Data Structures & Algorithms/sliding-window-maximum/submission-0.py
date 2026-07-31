class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        ans = []
        l = 0

        # Maintain a decreasing deque for the window.
        # Remove smaller elements that come before the larger one since they can never 
        # be max while a larger one exists.
        # They will always be removed before the larger element leaves the window 
        # so no need to keep them.
        
        for r in range(len(nums)):

            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])

            while r - l + 1 > k:
                if nums[l] == queue[0]:
                    queue.popleft()
                l += 1

            if r - l + 1 == k:
                ans.append(queue[0])


        return ans

        