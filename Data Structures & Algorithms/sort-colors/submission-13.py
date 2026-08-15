class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def _swap(arr, i , j):
            arr[i], arr[j] = arr[j], arr[i]

        low, high = 0, len(nums) - 1
        itr = 0

        while itr <= high:
            if nums[itr] == 0:
                _swap(nums, low, itr)
                low += 1
                itr += 1
            elif nums[itr] == 1:
                itr += 1
            elif nums[itr] == 2:
                _swap(nums, itr, high)
                high -= 1