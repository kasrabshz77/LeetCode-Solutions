class Solution(object):
    def maxProfit(self, prices):
        profit = 0 
        minimum = prices[0]
        for price in prices:
            if price < minimum:
                minimum = price

            if price - minimum > profit:
                profit = price - minimum

        return profit  

       

