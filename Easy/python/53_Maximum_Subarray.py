class Solution:
    def maxSubArray(nums):
        max_end = 0
        max_so = float('-inf')
        for i in range (len(nums)):
            max_end += nums[i]
            if max_so < max_end:
                max_so = max_end
            if max_end < 0:
                max_end = 0
        return max_so

print(Solution.maxSubArray([1]))
print(Solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution.maxSubArray([0]))
print(Solution.maxSubArray([-1]))
print(Solution.maxSubArray([-100000]))