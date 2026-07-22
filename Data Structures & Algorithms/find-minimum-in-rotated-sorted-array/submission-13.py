class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] > nums[-1]:
            low = 0
            high = len(nums) - 1

            while (low <= high):
                mid = low + (high - low)//2 

                if nums[mid] < nums[mid - 1]:
                    return nums[mid]
                elif nums[high] < nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        else:
            return nums[0]