class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        temp = sorted(set(nums))

        longest = 1
        for i in range(len(temp)):
            count = 1
            for j in range(i+1, len(temp)):
                if temp[j] - temp[j-1] == 1:
                    count += 1
                else:
                    break
            longest = max(longest, count)
        
        return longest