class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set()
        highest = 0

        for num in nums:
            numbers.add(num)
        
        for num in numbers:
            if not (num - 1) in numbers:
                length = 0
                current_number = num

                while (current_number in numbers):
                    length += 1
                    current_number += 1

                    if length > highest:
                        highest = length

        return highest