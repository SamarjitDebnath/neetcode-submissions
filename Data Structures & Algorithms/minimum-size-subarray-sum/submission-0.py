class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        _sum = 0
        min_len = float('inf')

        for r in range(len(nums)):
            _sum += nums[r]

            while _sum >= target:
                min_len = min(min_len, (r - l + 1))
                _sum -= nums[l]
                l += 1

        return min_len if min_len < float('inf') else 0