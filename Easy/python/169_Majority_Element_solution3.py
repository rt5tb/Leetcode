# Solution 3
# import collections.Counter
# find the element shows most in the array

import collections
class Solution:
    def majorityElement(nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

print(Solution.majorityElement([2,2,1,1,1,2,2]))
print(Solution.majorityElement([3,2,3]))