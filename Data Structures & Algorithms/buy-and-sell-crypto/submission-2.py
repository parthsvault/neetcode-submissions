class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[l] <= prices[r]:
                profit = max(profit, prices[r] - prices[l])
                r += 1
            
            elif prices[l] > prices[r]:
                l = r
                r = l + 1
            r 
            
        return profit