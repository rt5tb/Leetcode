# DP
class Solution:
    def maxProduct(nums):
        maxproduct = 0
        for i in range(len(nums)-1):
            j = i + 1
            for j in range(i+1, len(nums)):
                product = (nums[i] - 1) * (nums[j] - 1)
                maxproduct = max(product,maxproduct)
        return maxproduct

print(Solution.maxProduct(nums = [3,4,5,2]))
print(Solution.maxProduct(nums = [1,5,4,5]))
print(Solution.maxProduct(nums = [3,7]))

