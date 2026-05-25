class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Step 2: Create buckets where the index equals the frequency
        # We need len(nums) + 1 buckets to include index len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Step 3: Scan the buckets backward (from highest frequency to lowest)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                # Once we have collected k elements, we are done
                if len(result) == k:
                    return result