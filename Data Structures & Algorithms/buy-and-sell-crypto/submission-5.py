class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        h = 1
        maxP = 0

        while (h < len(prices)):
            if prices[h] < prices[l]:
                l = h
            else:
                maxP = max(prices[h] - prices[l], maxP)

            h += 1
                


        return maxP



