class Solution:
    def oddCells(n, m, indices):
        count = 0
        matrix = [[0 for i in range(m)] for j in range(n)]
        for i in indices:
            row = i[0]
            column = i[1]
            for k in range(m):
                matrix[row][k] += 1
            for l in range(n):
                matrix[l][column] +=1
        for i in matrix:
            for j in i:
                if j % 2 !=0:
                    count += 1
        return count

print(Solution.oddCells(n = 2, m = 3, indices = [[0,1],[1,1]]))
print(Solution.oddCells(n = 2, m = 2, indices = [[1,1],[0,0]]))