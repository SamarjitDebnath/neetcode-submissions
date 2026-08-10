class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # O(nlogn) --> logn for sort
        # if not nums:
        #     return 0
        
        # nums.sort()
        # longest = 1
        # current_max_streak = 1
        # i = 0
        # while i + 1 < len(nums):
        #     if nums[i+1] == nums[i] + 1:
        #         current_max_streak += 1
        #     elif nums[i+1] != nums[i]:
        #         longest = max(longest, current_max_streak)
        #         current_max_streak = 1
        #     i += 1
        # print(longest)
        # return max(longest, current_max_streak)
        
        # O(n) --> hashset
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest

