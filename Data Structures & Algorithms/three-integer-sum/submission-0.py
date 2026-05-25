class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        cache = {}

        for i in range(len(nums)):
            for v in range(i + 1, len(nums)):
                num1 = nums[i]
                num2 = nums[v]
                total = num1 + num2
                needed = -num1 - num2

                if needed in cache and cache[needed] != v and cache[needed] != i:
                    group = sorted([num1, num2, needed])
                    if not (group in triplets):
                        triplets.append(group)
                
                cache[num1] = i
                cache[num2] = v
        
        return triplets