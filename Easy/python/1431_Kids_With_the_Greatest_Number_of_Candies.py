class Solution:
    def kidsWithCandies(candies, extraCandies):
        maxcandy = max(candies)
        boollist = []
        for i in candies:
            if i + extraCandies >= maxcandy:
                boollist.append(True)
            else:
                boollist.append(False)
        return boollist



print(Solution.kidsWithCandies([2,3,5,1,3],3))
print(Solution.kidsWithCandies([4,2,1,1,2],1))
print(Solution.kidsWithCandies([12,1,12], 10))