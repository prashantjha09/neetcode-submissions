class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        min_price = prices[i]
        max_price = prices[j]
        profit = max_price - min_price
        max_len = len(prices)
        while i <= j and j < len(prices):
            tmp_profit = prices[j] - prices[i]
            profit = max(profit, tmp_profit)
            if j < max_len-1 and prices[j+1] < prices[i]:
                j+=1
                i = j
            else:
                j+=1
        return profit

        