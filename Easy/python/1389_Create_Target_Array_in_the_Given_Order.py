class Solution:
    def createTargetArray(nums, index):
        target = []
        for i in range(len(nums)):
            if len(target) > index[i]:
                target.insert(index[i], nums[i])
            else:
                target.append(nums[i])
        return target

print(Solution.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))
print(Solution.createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
print(Solution.createTargetArray(nums = [1], index = [0]))