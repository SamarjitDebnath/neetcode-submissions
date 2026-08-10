class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # l, r = 0, len(nums)-1

        # while l <= r:
        #     if nums[l] == val:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         r -= 1
        #     else:
        #         l += 1
        
        # return l

        pos = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[pos] = nums[i]
                pos += 1

        return pos