class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        bottom = row - 1
        left = 0
        right = col -1

        direction = 0 # 0: l -> r, 1: t -> b, 2: r -> l, 3: b -> t
        spiral = []
        while top <= bottom and left <= right:
            # left to right
            if direction == 0:
                for i in range(left, right+1):
                    spiral.append(matrix[top][i])
                top += 1
            
            # top to bottom
            elif direction == 1:
                for i in range(top, bottom+1):
                    spiral.append(matrix[i][right])
                right -= 1

            # right to left
            elif direction == 2:
                for i in range(right, left-1, -1):
                    spiral.append(matrix[bottom][i])
                bottom -= 1

            # bottom to top
            elif direction == 3:
                for i in range(bottom, top-1, -1):
                    spiral.append(matrix[i][left])
                left += 1
            
            direction = (direction + 1) % 4

        return spiral