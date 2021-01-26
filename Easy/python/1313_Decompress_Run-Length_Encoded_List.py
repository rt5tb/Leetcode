class Solution:
    def decompressRLElist(nums):
        res = []
        length = len(nums)//2
        for i in range(length):
            freq = nums[2*i]
            val = nums[2*i+1]
            for j in range(freq):
                res.append(val)
        return res
