class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        vote = 0

        for elem in nums:
            if vote == 0:
                candidate = elem

            vote += 1 if candidate == elem else -1

        return candidate

