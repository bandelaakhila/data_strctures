#best time to buy and sell stock
class solution:
    def maxProfit(self,prices):
        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
prices=list(map(int,input().split(',')))
sol=solution()
t1=sol.maxProfit(prices)
print(t1)
