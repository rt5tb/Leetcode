# Solution 1
# Step 1: get a set including unique elements of input
# step 2: majority means an element has more than half elements of input (y = at least half length of the input + 1)
# step 3: run a loop to find the element shows more than y in the input array
class Solution:
    def majorityElement(nums):
        x = set(nums)
        y = int(len(nums)/2) + 1
        for i in x:
            if nums.count(i) >= y:
                return i

print(Solution.majorityElement([2,2,1,1,1,2,2]))
print(Solution.majorityElement([3,2,3]))