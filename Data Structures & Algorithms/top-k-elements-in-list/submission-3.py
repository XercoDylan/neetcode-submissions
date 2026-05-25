class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        frequency = []

        for number in nums:
            if number in frequency_dict:
                frequency_dict[number] += 1
            else:
                frequency_dict[number] = 1 
        
        for num, num_frequency in frequency_dict.items():
            placed = False

            for i in range(len(frequency)):
                other_num = frequency[i]

                if frequency_dict[other_num] < num_frequency:
                    frequency.insert(i, num)
                    placed = True
                    break

            if placed == False:
                frequency.append(num)
                
        return frequency[0:k]
        