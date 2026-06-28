class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}

        for i in range(len(nums)):
            current = nums[i]
            needed = target - current

            if needed in previous:
                return [previous[needed], i]

            previous[current] = i