class Solution:
    def findNumbers(nums):
        count = 0
        for i in nums:
            if len(str(i))% 2 == 0:
                count +=1
        return count

print(Solution.findNumbers([555,901,482,1771]))