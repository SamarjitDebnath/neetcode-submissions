class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(m * n): n : length of piles, and m = max number of bananas
        # speed = 1

        # while True:
        #     total_time = 0
        #     for p in piles:
        #         total_time += math.ceil(p / speed)

        #     if total_time <= h:
        #         return speed
        #     speed += 1

        # return speed

        l, r = 1, max(piles)
        speed = r
        while l <= r:
            k =  l + (r - l) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)

            if total_time <= h:
                speed = min(speed, k)
                r = k - 1
            else:
                l = k + 1

        return speed