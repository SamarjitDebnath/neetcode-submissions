class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            extracted_bit = n & 1
            # res <<= 1
            res *= 2
            res |= extracted_bit
            # n >>= 1
            n //= 2
        return res