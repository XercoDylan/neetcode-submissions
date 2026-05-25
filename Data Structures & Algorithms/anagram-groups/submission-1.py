class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_groups = []
        def isAnagram(str1, str2):

            if len(str1) != len(str2):
                return False
            characters = {}
            for char in str1:
                if char in characters:
                    characters[char] += 1
                else:
                    characters[char] = 1
            
            for char in str2:
                if not (char in characters):
                    return False
                characters[char] -= 1
                if characters[char] <= 0:
                    del characters[char]
            
            return True
            

        
        while (len(strs) > 0):
            current_string = strs[0]
            group = [current_string]
            strs.pop(0)
            for i in range(len(strs) - 1, -1, -1):
                if isAnagram(current_string, strs[i]):
                    group.append(strs[i])
                    strs.pop(i)
            final_groups.append(group)

        return final_groups