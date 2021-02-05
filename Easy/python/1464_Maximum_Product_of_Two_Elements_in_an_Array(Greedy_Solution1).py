# Greedy Solution1
# using built-in sort
# return (nums[-1]-1) * (nums[-2]-1)
class Solution:
    def maxProduct(nums):
        nums.sort()
        return (nums[-1]-1) * (nums[-2]-1)

print(Solution.maxProduct(nums = [3,4,5,2]))
print(Solution.maxProduct(nums = [1,5,4,5]))
print(Solution.maxProduct(nums = [3,7]))