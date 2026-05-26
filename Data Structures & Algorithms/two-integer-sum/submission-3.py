class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                
        visited = {

        }

        for i in range(len(nums)):
            num = nums[i]
            needed = (target - num)
            if needed in visited:
                return [visited[needed], i]
            
            visited[num] = i