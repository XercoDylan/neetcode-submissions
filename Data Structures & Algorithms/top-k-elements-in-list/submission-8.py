class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}
        frequency_list = []

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        
        for i in range(0, k):
            highest = None

            for num, freq in frequency.items():
                if highest == None:
                    highest = num
                else:
                    if freq > frequency[highest]:
                        highest = num
            
            frequency_list.append(highest)

            del frequency[highest]


        return frequency_list

        
