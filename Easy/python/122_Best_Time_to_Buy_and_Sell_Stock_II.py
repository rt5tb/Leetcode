class Solution:
    def maxProfit(prices) :
        profit = 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                profit = profit + prices[i] - prices[i-1]
        return profit

print(Solution.maxProfit([7,6,4,3,1]))
print(Solution.maxProfit([7,1,5,3,6,4]))
print(Solution.maxProfit([1,2,3,4,5]))