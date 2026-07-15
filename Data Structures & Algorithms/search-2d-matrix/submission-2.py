class Solution:
    def binarySearch(self, row: List[int], target: int) -> bool:
        low = 0
        high = len(row) - 1

        while (low <= high):
            mid = low + (high - low)//2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                high = mid - 1 
            else:
                low = mid + 1 

        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                return self.binarySearch(row, target)

        return False