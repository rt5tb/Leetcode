class Solution:
    def smallerNumbersThanCurrent(nums):
        store = {}
        sortlist = sorted(nums)
        rel = []
        for i,n in enumerate(sortlist):
            if n not in store:
                store[n] = i
        for i in nums:
            rel.append(store[i])
        return rel

print(Solution.smallerNumbersThanCurrent([8,1,2,2,3]))
print(Solution.smallerNumbersThanCurrent([6,5,4,8]))
print(Solution.smallerNumbersThanCurrent([7,7,7,7]))