class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        frequency = {}
        low = 0
        high = 0
        longest = 0

        while (high < len(s)):
            high += 1
            index = high - 1
            current_letter = s[index] 

            if current_letter in frequency and  low <=  frequency[current_letter]  <= high:
                low = frequency[current_letter] + 1
                del frequency[current_letter]
            
            frequency[current_letter] = index
            longest = max(high - low, longest)





        return longest