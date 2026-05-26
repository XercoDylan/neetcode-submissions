class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_index = {

        }

        for i in range(len(numbers)):
            num = numbers[i]
            needed = target - num
            if (needed in numbers_index):
                return [numbers_index[needed] + 1, i + 1]

            numbers_index[num] = i