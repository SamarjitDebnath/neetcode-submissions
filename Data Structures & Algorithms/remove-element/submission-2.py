class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1
        k = 0
        while left <= right:
            if nums[left] != val:
                k += 1
                left += 1
            else:
                if nums[right] == val:
                    right -= 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
                    left += 1
                    k += 1

        return k
