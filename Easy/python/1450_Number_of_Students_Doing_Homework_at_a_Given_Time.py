class Solution:
    def busyStudent(startTime, endTime, queryTime):
        count = 0
        for i in range(len(startTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                count += 1
        return count

print(Solution.busyStudent(startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5))
print(Solution.busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4))
print(Solution.busyStudent(startTime = [4], endTime = [4], queryTime = 4))
print(Solution.busyStudent(startTime = [4], endTime = [4], queryTime = 5))
print(Solution.busyStudent(startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7))