class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_prices = [0] * len(prices)
        highest = 0

        for i in range(len(prices) - 1, -1, -1):
            if i == len(highest_prices) - 1:
                highest_prices[i] = prices[i]
            else:
                highest_prices[i] = highest_prices[i + 1] if highest_prices[i + 1] > prices[i] else prices[i]

        print(highest_prices)
        
        for i in range(0, len(prices)):
            max_price = highest_prices[i] - prices[i]

            if max_price > highest:
                highest = max_price
        

        return highest