class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0

        for elem in nums:
            if elem == 0:
                zeros += 1
            elif elem == 1:
                ones += 1
            else:
                twos += 1

        res = []
        res.extend([0] * zeros)
        res.extend([1] * ones)
        res.extend([2] * twos)

        nums[:] = res