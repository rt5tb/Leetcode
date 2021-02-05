import math
class Solution:
    def diagonalSum(mat):
        n = len(mat)
        d1 = 0
        d2 = 0
        for i in range(n):
            d1 += mat[i][i]
            d2 += mat[i][n-1-i]
        if n % 2 == 0:
            return d1 + d2
        else:
            mid = int(math.floor(n/2))
            return d1 + d2 - mat[mid][mid]

print(Solution.diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))
print(Solution.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution.diagonalSum([[5]]))