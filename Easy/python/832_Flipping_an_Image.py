class Solution:
    def flipAndInvertImage(A):
        n = len(A)
        if n % 2 == 0:
            mid = n // 2
            for i in A:
                for j in range(mid):
                    i[j], i[n-1-j] = i[n-1-j],i[j]
        else:
            mid = (n + 1)//2
            for i in A:
                for j in range(mid):
                    i[j], i[n-1-j] = i[n-1-j],i[j]
        for i in A:
            for j in range(n):
                if i[j] == 0:
                    i[j] = 1
                else:
                    i[j] = 0
        return A

print(Solution.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
print(Solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))