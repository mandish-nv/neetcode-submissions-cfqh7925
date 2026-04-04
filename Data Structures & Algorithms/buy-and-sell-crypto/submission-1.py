class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        temp = prices[:]
        for i in range(0, len(prices)):
            high = max(temp)
            diff = high - prices[i]
            if prices[i] != high and temp.index(prices[i]) < temp.index(high) and diff > maximum:
                maximum = diff

            temp.remove(temp[0])

        return maximum