class Solution:
    @staticmethod
    def countSetBits(num: int) -> int:
        count = 0
        while num:
            num &= num-1
            count += 1
        return count

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.countSetBits(i))
        return res