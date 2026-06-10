class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #buckets = [[]] * len(nums)
        buckets = [[] for _ in range(len(nums))]

        frequency_dict = {}

        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1

        
        for num, frequency in frequency_dict.items():
            buckets[frequency - 1].append(num)

        top_k = []

        for bucket in buckets:
            top_k = bucket + top_k



        return top_k[:k]
        