class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def _swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        low, high = 0, len(nums) - 1
        index = 0

        while index <= high:
            if nums[index] == 0:
                _swap(low, index)
                low += 1
                index += 1
            elif nums[index] == 1:
                index += 1
            else:
                _swap(index, high)
                high -= 1