class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        left = 0
        right = 0

        while (left < len(temperatures)):

            found = False
            while (right < len(temperatures)):
                if temperatures[right] > temperatures[left]:
                    result.append(right - left)
                    found = True
                    break
                right += 1
            
            if not (found):
                result.append(0)

            left += 1
            right = left + 1

        return result
        
        