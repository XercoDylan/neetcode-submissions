class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = set()


        for num in nums:
            if num in frequency:
                return True
            else:
                frequency.add(num)


        return False