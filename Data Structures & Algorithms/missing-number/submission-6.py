class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # _max = max(nums)
        # for i in range(0, _max):
        #     if i not in nums:
        #         return i
        # return _max+1
        
        # n = len(nums)
        # nums.sort()
        # for i in range(n):
        #     if nums[i] != i:
        #         return i
        # return n

        # res = len(nums)
        # for i in range(len(nums)):
        #     res += i - nums[i]
        # return res

        n = len(nums)
        res = n
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res