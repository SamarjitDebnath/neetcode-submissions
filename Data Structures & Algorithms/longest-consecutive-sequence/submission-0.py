class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        longest = 1
        current_max_streak = 1
        i = 0
        while i + 1 < len(nums):
            if nums[i+1] == nums[i] + 1:
                current_max_streak += 1
            elif nums[i+1] != nums[i]:
                longest = max(longest, current_max_streak)
                current_max_streak = 1
            i += 1
        return max(longest, current_max_streak)