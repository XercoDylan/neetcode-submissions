class Solution:
    def getChar(self, s: str):
        char = [0] * 26

        for n in s:
           char[ord(n) - ord("a")] += 1
    
        return tuple(char)

    def isAnagram(self, s: str, t: str) -> bool:
        return self.getChar(s) == self.getChar(t)
        