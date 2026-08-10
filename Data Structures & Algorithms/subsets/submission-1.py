class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def _dfs(start):
            res.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])  # choose
                _dfs(i + 1)         # backtrack
                subset.pop()            # unchoose
        _dfs(0)
        return res