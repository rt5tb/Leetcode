# Greedy
# use built in max function
# find first max and second max in nums
# return (max1-1) * (max2-1)
class Solution:
    def maxProduct(nums):
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        return (max1-1) * (max2-1)

print(Solution.maxProduct(nums = [3,4,5,2]))
print(Solution.maxProduct(nums = [1,5,4,5]))
print(Solution.maxProduct(nums = [3,7]))