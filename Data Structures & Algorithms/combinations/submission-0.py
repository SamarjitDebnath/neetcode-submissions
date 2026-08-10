class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []

        def _dfs(start):
            if len(subset) == k:
                res.append(subset.copy())
                return

            for i in range(start, n+1):
                subset.append(i)
                _dfs(i+1)
                subset.pop()

        _dfs(1)
        return res
