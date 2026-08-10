class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        left = 0
        right = len(height)-1

        leftMax, rightMax,  = height[left], height[right]
        waterTrap = 0
        while left <= right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                waterTrap += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                waterTrap += rightMax - height[right]
                right -= 1

        return waterTrap