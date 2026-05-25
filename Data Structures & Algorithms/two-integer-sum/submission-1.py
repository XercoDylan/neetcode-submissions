class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combinations = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in combinations:
                return [combinations[num], i]
            needed = target - num
            combinations[needed] = i
        
            
        