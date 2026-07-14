class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]

        frequency_dict = {}

        topk = []


        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        for num, frequency in frequency_dict.items():
            buckets[frequency - 1].append(num)

        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]

            if len(topk) == k:
                break
            
            for num in bucket:
                topk.append(num)

                if len(topk) == k:
                    break

        return topk

