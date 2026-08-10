class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == target:
        #             return True
        # return False

        # m, n = len(matrix), len(matrix[0])
        # row, col = 0, (n-1)
        # while row < m and col >= 0:
        #     if matrix[row][col] > target:
        #         col -= 1
        #     elif matrix[row][col] < target:
        #         row += 1
        #     else:
        #         return True
        # return False

        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n -1)

        while l <= r:
            mid = l + ((r - l) // 2)
            row, col = mid // n, mid % n
            if matrix[row][col] > target:
                r -= 1
            elif matrix[row][col] < target:
                l += 1
            else: return True
        return False


