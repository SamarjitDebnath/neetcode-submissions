class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def _dfs(start, remaining):
            if remaining == 0:
                res.append(subset.copy())
            
            for i in range(start, len(candidates)):
                if (i > start) and (candidates[i] == candidates[i - 1]):
                    continue

                if candidates[i] > remaining:
                    break

                subset.append(candidates[i])
                _dfs(i+1, (remaining - candidates[i]))
                subset.pop()

        _dfs(start=0, remaining=target)
        return res
                