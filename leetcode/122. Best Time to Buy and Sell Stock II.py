from typing import * 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # var to kep track of the profit 
        for i in range(1, len(prices)): # iterate over the list of prices 
            if prices[i] > prices[i-1]: # if price next day is bigger than current day 
                profit += prices[i] - prices[i-1] # sum the profits 
        return profit