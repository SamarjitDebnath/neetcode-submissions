class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        min_cap = r

        def isCapacity(cap):
            day, curr_cap = 1, cap

            for w in weights:
                if curr_cap - w < 0:
                    day += 1
                    curr_cap = cap
                curr_cap -= w
            return day <= days

        while l <= r:
            cap = (l + r) // 2
            if isCapacity(cap):
                min_cap = min(min_cap, cap)
                r = cap - 1
            else:
                l = cap + 1

        return min_cap