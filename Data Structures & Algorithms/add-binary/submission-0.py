class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binSum = []
        carry = 0

        indexA, indexB = len(a)-1, len(b)-1

        while indexA >= 0 or indexB >= 0 or carry > 0:
            if indexA >= 0:
                carry += int(a[indexA])
                indexA -= 1
            if indexB >= 0:
                carry += int(b[indexB])
                indexB -= 1
            
            binSum.append(str(carry & 1))
            carry >>= 1

        return ''.join(binSum[::-1])