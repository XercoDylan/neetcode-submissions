import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        num_freqs = []

        for num, freq in frequency.items():
            num_freqs.append((-freq, num))
        
        heapq.heapify(num_freqs)
        
        top_k = []
        for i in range(k):
            freq, num = heapq.heappop(num_freqs)
            top_k.append(num)

        return top_k