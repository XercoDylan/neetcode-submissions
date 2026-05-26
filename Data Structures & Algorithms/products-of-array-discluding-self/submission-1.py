class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        sufixes = []
        results = []

        for i in range(len(nums)):
            if not prefixes:
                prefixes.append(nums[i])
            else:
                prefixes.append(nums[i] * prefixes[i - 1])

        for i in range(len(nums) - 1, -1, -1):
            if not sufixes:
                sufixes.append(nums[i])
            else:
                sufixes.insert(0, nums[i] * sufixes[0])

        for i in range(len(nums)):
            sufix = 1
            prefix = 1

            if i > 0:
                prefix = prefixes[i - 1]
            
            if i < len(nums) - 1:
                sufix = sufixes[i + 1]

            results.append(prefix * sufix)
        
        return results
            
        