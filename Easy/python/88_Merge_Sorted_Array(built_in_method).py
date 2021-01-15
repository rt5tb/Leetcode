# Built in Method
class Solution:
    def merge(nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1

print(Solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(Solution.merge(nums1 = [1], m = 1, nums2 = [], n = 0))