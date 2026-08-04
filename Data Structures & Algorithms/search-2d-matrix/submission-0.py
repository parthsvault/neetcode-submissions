class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid_r = (l + r) //2
            if target < matrix[mid_r][0]:
                r = mid_r - 1
            
            elif target > matrix[mid_r][-1]:
                l = mid_r + 1

            elif matrix[mid_r][0] <= target and target <= matrix[mid_r][-1]:
                break 
        else:
            return False

        l = 0
        r = len(matrix[mid_r]) - 1

        while l <= r:
            mid_c = (l + r) //2

            if target == matrix[mid_r][mid_c]:
                return True

            if target <= matrix[mid_r][mid_c]:
                r = mid_c - 1

            elif  target > matrix[mid_r][mid_c]:
                l = mid_c + 1
           
        
        return False
