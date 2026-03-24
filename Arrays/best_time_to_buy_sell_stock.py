#Brute Force Approach O(n^2)
def maxProfit(prices):
    max_profit = 0
    
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
                
    return max_profit

#Optimized Approach O(n)
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

prices = [7,2,1,5,6,8]
print(maxProfit(prices))
                