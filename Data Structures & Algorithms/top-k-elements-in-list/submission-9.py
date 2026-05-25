class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}
        buckets = [[] for _ in nums]
        frequency_list = []

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        for num, freq in frequency.items():
            buckets[freq - 1].append(num)

        print(buckets)
        for i in range(len(buckets) - 1, -1, -1):
            frequency_list += buckets[i]

            if len(frequency_list) >= k:
                break
 
        

        return frequency_list[0:k]

        
