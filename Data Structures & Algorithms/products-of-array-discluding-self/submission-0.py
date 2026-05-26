class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        sufixes = []
        result = []

        for i in range(len(nums)):
            if not prefixes:
                prefixes.append(nums[i])
            else:
                prefixes.append(nums[i] * prefixes[i - 1])
        
        for i in range(len(nums) - 1, -1, -1):
            if not sufixes:
                sufixes.insert(0, nums[i])
            else:
                sufixes.insert(0, nums[i] * sufixes[0])
        
        print(prefixes)
        print(sufixes)
        for i in range(len(nums)):
            prefix = 1
            sufix = 1

            if i > 0:
                prefix = prefixes[i - 1]

            if i < len(nums) - 1:
                sufix = sufixes[i + 1]

            print(f"{nums[i]},{sufix},{prefix}")

            result.append(sufix * prefix)

        return result
            


        

         
        