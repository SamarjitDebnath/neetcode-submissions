class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch National Flag Algorithm
        low, high = 0, len(nums) - 1
        mid = 0
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while mid <= high:
            if nums[mid] == 0:
                swap(mid, low)
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            elif nums[mid] == 2:
                swap(mid, high)
                high -= 1