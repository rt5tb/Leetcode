import itertools
class Solution:
    def numIdenticalPairs(nums):
        n = len(nums)
        a = list(range(0,n))
        comb = itertools.combinations(a,2)
        count = 0
        for i in comb:
            if nums[i[0]] == nums[i[1]]:
                count = count + 1
        return count

print(Solution.numIdenticalPairs([1,2,3,1,1,3]))
print(Solution.numIdenticalPairs([1,1,1,1]))
print(Solution.numIdenticalPairs([1,2,3,1,1,3]))