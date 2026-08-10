class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def _isPalindrome(string: str) -> bool:
            return string == string[::-1]

        res = []
        subset = []

        def _dfs(start):
            if start == len(s):
                res.append(subset.copy())
                return

            for i in range(start, len(s)):
                if _isPalindrome(s[start : i+1]):
                    subset.append(s[start : i+1])
                    _dfs(i + 1)
                    subset.pop()

        _dfs(0)
        return res
                    
