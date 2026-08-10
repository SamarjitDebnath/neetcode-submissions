class Solution:
    def validPalindrome(self, s: str) -> bool:
        def _isPanlindrome(l, r):
            return s[l:r+1] == s[l:r+1][::-1]
        
        if s == s[::-1]:
            return True

        l, r = 0, len(s)-1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if _isPanlindrome(l+1, r):
                    l += 1
                elif _isPanlindrome(l, r-1):
                    r -= 1
                else:
                    return False
        return True