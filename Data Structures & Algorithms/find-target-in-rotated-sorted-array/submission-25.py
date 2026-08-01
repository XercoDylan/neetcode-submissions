class Solution:
    def getMinimum(self, nums: List[int]):
        if nums[-1] > nums[0] or len(nums) == 1:
            return 0
        
        low = 0
        high = len(nums) - 1

        while (low <= high):
            mid = low + (high - low)//2

            if nums[mid] < nums[mid - 1]:
                return mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1

        

    def search(self, nums: List[int], target: int) -> int:

        minimum_index = self.getMinimum(nums)
        minumum = nums[minimum_index]

        low = minimum_index if minumum <= target <= nums[-1] else 0
        high = len(nums) - 1 if minumum <= target <= nums[-1] else minimum_index - 1


        while (low <= high):
            mid = low + (high - low)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1