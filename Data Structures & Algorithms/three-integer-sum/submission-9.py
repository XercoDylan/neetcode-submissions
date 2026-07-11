class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        triplets = []

        for i in range(len(sorted_nums)):
            current_num = sorted_nums[i]

            if i != 0 and current_num == sorted_nums[i - 1]:
                continue
            
            k = i + 1
            j = len(sorted_nums) - 1

            while (j > k):
                value = sorted_nums[k] + sorted_nums[j]
                if value > -current_num:
                    j -= 1
                elif value < -current_num:
                    k += 1
                elif value == -current_num:
                    triplets.append([current_num, sorted_nums[k] , sorted_nums[j]])
                    
                    k += 1
                    j -= 1

                    while k < j and sorted_nums[k] == sorted_nums[k - 1]:
                        k += 1

                    while j > k and sorted_nums[j] == sorted_nums[j + 1]:
                        j -= 1
                    

    
        



        return triplets