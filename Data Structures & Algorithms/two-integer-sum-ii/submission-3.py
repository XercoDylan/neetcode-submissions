class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_index = {

        }

        for i in range(len(numbers)):
            num = numbers[i]
            if not (num in numbers_index):
                numbers_index[num] = i + 1

        for i in range(len(numbers)):
            num = numbers[i]
            needed = target - num

            if needed in numbers_index:
                if numbers_index[needed] > i:
                    return [i + 1, numbers_index[needed]]
                else:
                    return [numbers_index[needed], i + 1]
