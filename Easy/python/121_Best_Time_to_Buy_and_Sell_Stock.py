class Solution:
    def maxProfit(prices):
        temp = float('inf')
        comp = 0
        for i in (prices):
            if i < temp:
                temp = i
            else:
                comp = max(comp, i - temp)
        return comp

print(Solution.maxProfit([7,6,4,3,1]))
print(Solution.maxProfit([7,1,5,3,6,4]))