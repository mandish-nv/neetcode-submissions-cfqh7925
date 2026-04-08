class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        size = len(matrix) 
        left = 0
        right = size - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                if  mid - 1 >= 0 and matrix[mid - 1][0] < target:
                    mid = mid - 1
                    break 
                right = mid - 1
            elif matrix[mid][0] < target:
                if  mid + 1 <= size - 1 and matrix[mid + 1][0] > target:
                    mid = mid
                    break 
                left = mid + 1

        print(f"Matrix location: {mid}")
        t_matrix = matrix[mid]
        size = len(t_matrix) 
        left = 0
        right = size - 1

        while left <= right:
            mid = (left + right) // 2
            if t_matrix[mid] == target:
                return True
            elif t_matrix[mid] > target:
                right = mid - 1
            elif t_matrix[mid] < target:
                left = mid + 1

        return False
