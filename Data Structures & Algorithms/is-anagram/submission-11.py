class Solution:

    def getLetters(self, s: str):
        letters = [0] * 26

        for letter in s:
            letters[ord(letter)%97] += 1

        
        return letters





    def isAnagram(self, s: str, t: str) -> bool:
        return self.getLetters(s) == self.getLetters(t)
        