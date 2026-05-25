class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = []
        for number in nums:
            if number in duplicates:
                return True
            duplicates.append(number)
        
        return False
        