class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i, d in enumerate(digits[::-1]):
            idx = len(digits) - 1 - i
            if d == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        
        digits[0] = 1
        digits.append(0)

        return digits