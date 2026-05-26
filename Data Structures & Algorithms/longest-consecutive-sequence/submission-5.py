class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set()

        for num in nums:
            if not (num in elements):
                elements.add(num)

        largest = 0

        for num in elements:
            current_length = 1
            if (num + 1) in elements and not ((num - 1) in elements):
                current_length = 2
                current_num = num + 2

                while (current_num in elements):
                    current_num += 1
                    current_length += 1
                
            if current_length > largest:
                largest = current_length

        return largest



        
