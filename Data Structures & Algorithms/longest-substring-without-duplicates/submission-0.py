class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStr = set()
        l = 0
        max_length = 0
        
        for r in range(len(s)):
            # If the character is already in the set, slide the left pointer
            while s[r] in subStr:
                subStr.remove(s[l])
                l += 1
            
            # Add the current character to the set
            subStr.add(s[r])
            
            # Update the maximum length
            max_length = max(max_length, r - l + 1)
        
        return max_length