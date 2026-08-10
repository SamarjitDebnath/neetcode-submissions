class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2147483647
        min_int = -2147483647

        negation = False
        if x < 0:
            negation = True
            x = abs(x)
        res = 0
        while x:
            remainder = x % 10
            res = res * 10 + remainder
            x //= 10
        print(negation)
        if negation:
            res = res * -1
        
        return res if res >= min_int and res <= max_int else 0