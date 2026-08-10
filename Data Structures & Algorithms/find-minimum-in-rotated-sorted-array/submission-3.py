class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_elem = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                min_elem = min(min_elem, nums[l])
                break

            mid = l + (r - l) // 2
            min_elem = min(min_elem, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return min_elem