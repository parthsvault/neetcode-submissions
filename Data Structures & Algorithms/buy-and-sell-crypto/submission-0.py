class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for sell in range(len(prices)):
            buy = 0
            while buy <= sell:
                cur_profit = prices[sell] - prices[buy]
                if profit < cur_profit:
                    profit = cur_profit
                
                buy += 1

        return profit