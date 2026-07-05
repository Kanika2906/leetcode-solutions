class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        maxP = 0
        for price in prices:
            profit = price - min_buy
            if profit>maxP:
                maxP = profit
            min_buy = min(min_buy,price)
        return maxP