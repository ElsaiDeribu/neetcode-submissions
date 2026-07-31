class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # time = pile/ rate
        left, right = 1, max(piles)

        def check(rate):
            
            total_time_taken = 0
            for pile in piles:
                total_time_taken += math.ceil(pile / rate)

            return total_time_taken


        while left <= right:
            mid = (left + right) // 2

            if check(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1


        return left

