class Solution:
    def containsDuplicate(nums):
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False



print(Solution.containsDuplicate([2,14,18,22,22]))
print(Solution.containsDuplicate([1,2,3,4]))
print(Solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))