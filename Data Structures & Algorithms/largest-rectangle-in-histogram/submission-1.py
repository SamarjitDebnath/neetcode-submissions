class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Time: O(n^2), Space: O(1)
        # n = len(heights)
        # max_area = 0

        # # Iterate through each bar as the starting point
        # for i in range(n):
        #     # Find the minimum height between bars i and j
        #     min_height = heights[i]

        #     # Check all possible rectangles extending from index i
        #     for j in range(i, n):
        #         min_height = min(min_height, heights[j])
        #         width = j - i + 1   
        #         max_area = max(max_area, (min_height * width))
        
        # return max_area

        # Monotic Increasing Stack, Time: O(n), Space: O(n)
        maxArea = 0
        stack = [] #[index, height]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea





