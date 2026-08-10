class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # window = set()
        # for i in range(len(nums)):
        #     if nums[i] in window:
        #         return True
            
        #     window.add(nums[i])

        #     if len(window) > k:
        #         window.remove(nums[i-k])

        # return False

        for i in range(len(nums)):
            for j in range(i+1, min(len(nums), i+k+1)):
                if nums[i] == nums[j]:
                    return True
        return False