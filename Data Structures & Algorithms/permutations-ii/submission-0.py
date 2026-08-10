class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        perm = []
        path = []
        used = [False] * n

        def _backtrack():
            if len(path) == n:
                perm.append(path.copy())
                return

            for i in range(n):
                if used[i]:
                    continue
    
                if i > 0 and (nums[i] == nums[i - 1]) and not used[i - 1]:
                    continue
                
                # choose
                used[i] = True
                path.append(nums[i])

                # recurse
                _backtrack()

                # unchoose
                used[i] = False
                path.pop()
        
        _backtrack()
        return perm