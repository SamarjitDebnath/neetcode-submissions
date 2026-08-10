class Solution:
    def hammingWeight(self, n: int) -> int:
        set_bits = 0
        while n:
            n = n & (n-1)
            set_bits += 1
        return set_bits