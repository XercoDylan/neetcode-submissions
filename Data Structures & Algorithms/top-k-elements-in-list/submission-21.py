import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for num, freq in frequency.items():
            buckets[freq - 1].append(num)

        top_k = []


        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k

        