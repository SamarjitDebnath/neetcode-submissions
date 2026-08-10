class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        l, r = 0, x // 2
        while l <= r:
            mid = (l + r) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                r = mid - 1
            else:
                l = mid + 1
        return int(r)