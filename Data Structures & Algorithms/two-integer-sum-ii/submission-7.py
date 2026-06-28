class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num1 = 0
        num2 = len(numbers) - 1

        while (numbers[num1] + numbers[num2] != target):
            if numbers[num1] + numbers[num2] > target:
                num2 -= 1
            else:
                num1 += 1




        return [num1 + 1, num2 + 1]
        