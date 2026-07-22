class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = float("inf")

        for p in prices:
            if p < min_p:
                min_p = p
            elif (p - min_p) > profit:
                profit = p - min_p

        return profit
            