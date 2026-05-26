class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_index = {

        }

        for i in range(len(numbers)):
            num = numbers[i]
            if num in numbers_index:
                numbers_index[num].append(i + 1)
            else:
                numbers_index[num] = [i + 1]

        for i in range(len(numbers)):
            num = numbers[i]
            needed = target - num

            if needed in numbers_index:
                for index in numbers_index[needed]:
                    if index > i:
                        return [i + 1, index]
                    else:
                        return [index, i + 1]
