class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     nums.insert(i+n, nums[i])
        # return nums

        # nums += nums

        nums.extend(nums)

        return nums