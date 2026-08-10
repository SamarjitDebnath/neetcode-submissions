class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res = abs(nums[i])
                break
            nums[idx] *= -1

        return res