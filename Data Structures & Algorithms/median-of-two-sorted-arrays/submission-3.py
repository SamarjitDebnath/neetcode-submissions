class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(A)-1
        while True: # for sure there's a median
            # cut of A, mid of l and r
            i = (l + r) // 2
            # cut of B, that ensures length of elems in left of A and B is half
            j = half - i - 2

            # comparison and elemnt selection
            Aleft = A[i] if i >= 0 else -float('infinity')
            Aright = A[i+1] if i+1 < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else -float('infinity')
            Bright = B[j+1] if j+1 < len(B) else float('infinity')

            # found the median? | Partition is valid?
            if Aleft <= Bright and Bleft <= Aright:
                # number of element is odd
                if total % 2:
                    return min(Aright, Bright)
                # number of elemnt is even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            else:
                if Aleft < Bright:
                    l = i + 1
                else:
                    r = i - 1