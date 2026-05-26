class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        sufixes = [0] * len(nums)
        results = []

        for i in range(len(nums)):
            if not prefixes:
                prefixes.append(nums[i])
            else:
                prefixes.append(nums[i] * prefixes[i - 1])
        
        current_sufix = 1
        for i in range(len(nums) - 1, -1, -1):
            sufixes[i] = current_sufix * nums[i]
            current_sufix = sufixes[i]

        for i in range(len(nums)):
            sufix = 1
            prefix = 1

            if i > 0:
                prefix = prefixes[i - 1]
            
            if i < len(nums) - 1:
                sufix = sufixes[i + 1]

            results.append(prefix * sufix)
        
        return results
            
        