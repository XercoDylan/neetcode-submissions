class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        sufix = [nums[-1]]
        output = []

        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[-1])
        
        for i in range(len(nums) - 2, -1, -1):
            sufix.append(nums[i] * sufix[-1])

        
        print(prefix)
        print(sufix)


        for i in range(len(nums)):
            before = 1

            if i > 0:
                before = prefix[i - 1]


            after = 1

            if i < len(nums) - 1:
                after = sufix[(len(nums) - 2) - i]

            output.append(before * after)

        return output






