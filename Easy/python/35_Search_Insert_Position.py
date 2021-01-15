class Solution:
    def searchInsert(nums, target):
        if nums[-1] < target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

print(Solution.searchInsert([1,3,5,6],5))
print(Solution.searchInsert([1,3,5,6],2))
print(Solution.searchInsert([1,3,5,6],7))
print(Solution.searchInsert([1,3,5,6],0))
print(Solution.searchInsert([1],0))