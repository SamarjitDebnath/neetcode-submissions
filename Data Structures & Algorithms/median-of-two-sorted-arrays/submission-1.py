class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # brute force
        if not nums1 and not nums2:
            return
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        merged_nums = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged_nums.append(nums1[i])
                i += 1
            else:
                merged_nums.append(nums2[j])
                j += 1

        while i < m:
            merged_nums.append(nums1[i])
            i += 1
        while j < n:
            merged_nums.append(nums2[j])
            j += 1
        print(f"DEBUG - {merged_nums}")
        
        median = 0.0
        if (m+n) % 2 != 0:
            median = merged_nums[(m+n)//2]
        else:
            median = (merged_nums[((m+n)//2)-1] + merged_nums[(m+n)//2]) / 2

        return median