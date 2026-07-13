class Solution:
    def binarySearch(self, nums: List[[int]], target: int):
        high = len(nums) - 1
        low = 0

        while (low <= high):
            mid = (high + low)//2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1

        return False



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            if nums[0] <= target <= nums[-1]:
                return self.binarySearch(nums, target)

        return False