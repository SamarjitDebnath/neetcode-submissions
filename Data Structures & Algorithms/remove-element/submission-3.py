class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)-1
        k = 0
        while l <= r:
            if nums[l] != val:
                k += 1
                l += 1
            else:
                if nums[r] == val:
                    r -= 1
                else:
                    nums[l], nums[r] = nums[r], nums[l]
                    r -= 1
                    l += 1
                    k += 1
        
        return k
