class Solution:
    def containsDuplicate(nums):
        a = set(nums)
        if len(a) == len(nums):
            return False
        else:
            return True

        # return len(set(nums)) != len(nums)
        # return len(set(nums)) < len(nums)


print(Solution.containsDuplicate([2,14,18,22,22]))
print(Solution.containsDuplicate([1,2,3,4]))
print(Solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))