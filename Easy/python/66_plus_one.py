class Solution:
    def plusOne(digits):
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
        return [1] + digits

print(Solution.plusOne([7,9,9]))
print(Solution.plusOne(digits = [1,2,3]))
print(Solution.plusOne(digits = [4,3,2,1]))
print(Solution.plusOne(digits = [0]))