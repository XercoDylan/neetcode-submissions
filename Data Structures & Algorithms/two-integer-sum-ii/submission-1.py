class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}

        for i in range(len(numbers)):
            num = numbers[i]
            needed = target - num
            if needed in cache and cache[needed] != i:
                return [cache[needed] + 1, i + 1]
            cache[num] = i
        