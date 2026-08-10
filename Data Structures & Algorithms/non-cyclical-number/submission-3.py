class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquareOfDigits(num: int) -> int:
            res = 0
            while num:
                res += (num % 10) ** 2
                num //= 10
            return res

        # seen = set()
        # while n != 1:
        #     if n in seen:
        #         return False
        #     seen.add(n)
        #     n = sumSquareOfDigits(n)

        # return True

        slow = n
        fast = sumSquareOfDigits(n)

        while fast != 1 and slow != fast:
            slow = sumSquareOfDigits(slow)
            fast = sumSquareOfDigits(sumSquareOfDigits(fast))

        return fast == 1