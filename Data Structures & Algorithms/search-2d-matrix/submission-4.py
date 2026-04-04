class Solution:

    # def binarySearch(self, lst, target):
    #     left = 0
    #     right = len(lst) - 1
    #     while left <= right:

    # # my implementation: O(m+n)
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     # 1. get matrix size
    #     rows = len(matrix)
    #     cols = len(matrix[0])

    #     # boundary check
    #     if rows == 0 or cols == 0:
    #         return False

    #     # 2. iterate through first and last element of each row to find target row
    #     target_row = -1
    #     for i in range(rows):
    #         if matrix[i][0] <= target and matrix[i][cols-1] >= target:
    #             target_row = i
    #             break
    #     if target_row == -1:
    #         return False
        
    #     # 3. iterate target row to check (better with binary search)
    #     for j in range (cols):
    #         if matrix[target_row][j] == target:
    #             return True
    #     return False

    # O(log(m*n))
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // cols][mid % cols]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False