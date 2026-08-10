class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # brute force- Time: O(m+n), Space: O(m+n)
        # if not nums1 and not nums2:
        #     return
        # m, n = len(nums1), len(nums2)
        # i, j = 0, 0
        # merged_nums = []
        # while i < m and j < n:
        #     if nums1[i] < nums2[j]:
        #         merged_nums.append(nums1[i])
        #         i += 1
        #     else:
        #         merged_nums.append(nums2[j])
        #         j += 1

        # while i < m:
        #     merged_nums.append(nums1[i])
        #     i += 1
        # while j < n:
        #     merged_nums.append(nums2[j])
        #     j += 1
        # print(f"DEBUG - {merged_nums}")
        
        # median = 0.0
        # if (m+n) % 2 != 0:
        #     median = merged_nums[(m+n)//2]
        # else:
        #     median = (merged_nums[((m+n)//2)-1] + merged_nums[(m+n)//2]) / 2

        # return median

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # for A
            j = half - i - 2 # for B

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if (i+1) < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j+1] if (j+1) < len(B) else float('infinity')

            # correct partition
            if Aleft <= Bright and Bleft <= Aright:
                # odd number of elements
                if total % 2:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2       
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1