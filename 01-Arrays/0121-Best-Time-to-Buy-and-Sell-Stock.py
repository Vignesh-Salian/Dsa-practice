# Difficulty: Easy
# Topic: Greedy + Min Tracking
# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

def maxProfit(prices):
    min_price=float("inf")
    max_profit=0
    n=len(prices)
    for i in range(0,n):
        min_price=min(prices[i], min_price)
        max_profit=max(max_profit,prices[i]-min_price)
    return max_profit

prices = [7,6,4,3,1]
print(maxProfit(prices))