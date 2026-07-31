class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        running_min = float("inf")
        profit = 0

        for price in prices:
            running_min = min(running_min, price)
            profit = max(profit, price - running_min)


        return profit
    