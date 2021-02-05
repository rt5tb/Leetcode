class Solution:
    def minTimeToVisitAllPoints(points):
        count = 0
        for i in range(1, len(points)):
            if abs(points[i-1][0] - points[i][0]) >= abs(points[i-1][1] - points[i][1]):
                count += abs(points[i-1][0] - points[i][0])
            else:
                count += abs(points[i-1][1] - points[i][1])
        return count

print(Solution.minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]]))
print(Solution.minTimeToVisitAllPoints(points = [[3,2],[-2,2]]))