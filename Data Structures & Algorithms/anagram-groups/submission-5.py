class Solution:
    def getChar(self, s: str):
        char = [0] * 26

        for n in s:
            char[ord(n) - ord("a")] += 1

        return tuple(char)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        cache = {}

        for string in strs:
            char = self.getChar(string)

            if char in cache:
                cache[char].append(string)
            else:
                new_group = [string]
                groups.append(new_group)
                cache[char] = new_group

        return groups

