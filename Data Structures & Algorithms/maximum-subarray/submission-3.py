class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')

        max_ending = 0

        for i in range(len(nums)):
            max_ending += nums[i]
            res = max(res, max_ending)
            if max_ending < 0 :
                max_ending = 0

        return res