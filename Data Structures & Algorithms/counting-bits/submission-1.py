class Solution:
    def countBits(self, n: int) -> List[int]:
        def setBits(num: int) -> int:
            count = 0
            while num:
                num &= num - 1
                count += 1
            return count

        return [setBits(i) for i in range(n+1)]
