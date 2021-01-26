class Solution:
    def xorOperation(n, start):
        target = 0
        for i in range(n):
            target ^= start+2*i
        return target

print(Solution.xorOperation(n = 5, start = 0))
print(Solution.xorOperation(n = 4, start = 3))
print(Solution.xorOperation(n = 1, start = 7))
print(Solution.xorOperation(n = 10, start = 5))