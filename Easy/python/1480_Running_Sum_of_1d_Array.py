class Solution:
    def runningSum(nums):
        sumlist = []
        sumsofar = 0
        for i in range(len(nums)):
            sumsofar = sumsofar + nums[i]
            sumlist.append(sumsofar)
        return sumlist

print(Solution.runningSum([1,2,3,4]))
print(Solution.runningSum([1,1,1,1,1]))
print(Solution.runningSum([3,1,2,10,1]))