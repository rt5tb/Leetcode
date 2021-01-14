class Solution:
    def twoSum(nums, target):
        a = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in a:
                a[num] = i
            else:
                return[a[n],i]

print(Solution.twoSum([2,7,11,15], 9))
print(Solution.twoSum([3,2,4], 6))
print(Solution.twoSum([3,3], 6))