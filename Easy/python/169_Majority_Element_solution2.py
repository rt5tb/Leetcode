# Solution 2
# if existing one element shows more than half in the array
# when the array is sorted
# the value at mid must be the majority element of the array

class Solution:
    def majorityElement(nums):
        nums.sort()
        return nums[len(nums)//2]

print(Solution.majorityElement([2,2,1,1,1,2,2]))
print(Solution.majorityElement([3,2,3]))