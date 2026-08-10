class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Time: O(max(piles) * len(piles)) ==> O(m*n)
        # TLE
        # rate = 1
        # while True:
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile/rate)
            
        #     if totalTime <= h:
        #         return rate
        #     rate += 1
        # return rate

        # Binary Search, Time: O(n * log(m))
        l, r = 1, max(piles)
        rate = r
        
        while l <= r:
            k = l + (r - l) // 2
            
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/k)

            if totalTime <= h:
                rate = k
                r = k - 1
            else:
                l = k + 1
        return rate
