# it can also use algorithm I used in 1_Two_sum
# it is a general method to solve two sum problem with input (sorted or unsorted)
# Here I used two pointers for the sorted input
class Solution:
    def twoSum(numbers, target):
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]

print(Solution.twoSum([2,7,11,15],9))
print(Solution.twoSum([2,3,4],6))
print(Solution.twoSum([-1,0],-1))