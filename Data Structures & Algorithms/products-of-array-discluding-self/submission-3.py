class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        sufix = [nums[-1]]
        output = []

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i])

        for i in range(len(nums) - 2, -1, -1):
            sufix.append(sufix[-1] * nums[i])

        print(prefix)
        print(sufix)

        for i in range(len(nums)):
            prefix_num = 1 if i == 0 else prefix[i - 1]
            sufix_num = 1 if i == len(nums) - 1 else sufix[len(nums) - 2 - i]

            output.append(prefix_num * sufix_num)

        return output

