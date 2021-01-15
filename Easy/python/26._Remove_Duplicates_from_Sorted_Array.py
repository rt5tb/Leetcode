# 2 pointers method
class Solution:
    def removeDuplicates(nums):
        index = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index

print(Solution.removeDuplicates([1,1,2]))
print(Solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))