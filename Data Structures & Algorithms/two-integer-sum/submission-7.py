class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            num = nums[i]
            needed = target - num
            if needed in freq:
                return [freq[needed], i]
            
            freq[num] = i

