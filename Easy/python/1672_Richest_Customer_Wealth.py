class Solution:
    def maximumWealth(accounts):
        tempmax = 0
        for i in accounts:
            if tempmax < sum(i):
                tempmax = sum(i)
        return tempmax

print(Solution.maximumWealth([[1,2,3],[3,2,1]]))
print(Solution.maximumWealth([[1,5],[7,3],[3,5]]))
print(Solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))