class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [ [] for _ in range(len(nums))]

        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for num, amount in frequency.items():
            buckets[amount - 1].append(num)

        output = []

        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]

            if len(output) >= k:
                break

            output += bucket

        return output[:k]