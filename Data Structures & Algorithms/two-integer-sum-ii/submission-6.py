class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointers = [0, len(numbers) - 1]

        while ( (numbers[pointers[1]] +  numbers[pointers[0]]) != target):
            if (numbers[pointers[1]] +  numbers[pointers[0]]) > target:
                pointers[1] -= 1
            else:
                pointers[0] += 1

        return [pointers[0] + 1, pointers[1] + 1]