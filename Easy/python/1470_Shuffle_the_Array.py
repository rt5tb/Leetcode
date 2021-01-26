class Solution:
    def shuffle(nums, n):
        reorder = []
        for i in range(n):
            reorder.append(nums[i])
            reorder.append(nums[i + n])
        return reorder

print(Solution.shuffle([2,5,1,3,4,7],3))
print(Solution.shuffle([1,2,3,4,4,3,2,1],4))
print(Solution.shuffle([1,1,2,2],2))